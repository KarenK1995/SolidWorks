import cadquery as cq
from cadquery import exporters

# Dimensions in millimeters
base_length = 8000  # 8 m
base_width = 6000   # 6 m
base_height = 3000  # 3 m
roof_height = 2000  # 2 m from top of base
wall_thickness = 200

def make_base():
    base = cq.Workplane("XY").box(base_length, base_width, base_height, centered=(True, True, False))

    interior = (
        cq.Workplane("XY")
        .box(
            base_length - 2 * wall_thickness,
            base_width - 2 * wall_thickness,
            base_height - wall_thickness,
            centered=(True, True, False),
        )
        .translate((0, 0, wall_thickness))
    )

    shell = base.cut(interior)

    door = (
        cq.Workplane("XY", origin=(-base_length / 2 + wall_thickness + 900, 0, 0))
        .rect(900, wall_thickness * 1.5)
        .workplane(offset=2100)
        .rect(900, wall_thickness * 1.5)
        .loft(combine=True)
        .translate((0, base_width / 2, 0))
    )

    window_profile = (
        cq.Workplane("XY")
        .center(0, base_width / 2 - wall_thickness / 2)
        .rect(1200, wall_thickness)
        .workplane(offset=1200)
        .rect(1200, wall_thickness)
        .loft(combine=True)
        .translate((0, 0, 1000))
    )

    windows = window_profile.union(window_profile.translate((0, -base_width + wall_thickness, 0)))

    base_with_openings = shell.cut(door).cut(windows)

    return base_with_openings


def make_roof():
    roof_profile = (
        cq.Workplane("XZ")
        .polyline([
            (-base_length / 2, base_height),
            (0, base_height + roof_height),
            (base_length / 2, base_height),
            (-base_length / 2, base_height),
        ])
        .close()
    )

    roof = roof_profile.extrude(base_width, both=False)

    roof = roof.translate((0, 0, 0))
    return roof


def make_floor_slab():
    slab = (
        cq.Workplane("XY")
        .box(base_length + 200, base_width + 200, 200, centered=(True, True, False))
    )
    return slab


def export_models():
    base = make_base()
    roof = make_roof()
    slab = make_floor_slab()

    exporters.export(base, "output/House_Base.step")
    exporters.export(roof, "output/House_Roof.step")
    exporters.export(slab, "output/House_Floor.step")

    assembly = cq.Assembly(name="House")
    assembly.add(base, name="Base")
    assembly.add(roof.translate((0, 0, 0)), name="Roof")
    assembly.add(make_floor_slab(), name="Floor", loc=cq.Location((0, 0, -200)))

    assembly.save("output/House_Assembly.step")


if __name__ == "__main__":
    export_models()
