# Demo House SolidWorks Assets

This folder contains neutral CAD files created with [CadQuery](https://github.com/CadQuery/cadquery) that can be imported into SolidWorks to demonstrate a simple house assembly.

## Contents

- `House_Base.step` – The hollow wall structure with door and window openings.
- `House_Roof.step` – A gable roof solid sized to sit on top of the base walls.
- `House_Floor.step` – A concrete slab style floor plate slightly larger than the house footprint.
- `House_Assembly.step` – All three parts positioned together as an assembly reference.

## Usage

1. Open SolidWorks and import the `.step` parts via **File → Open** and choose `STEP AP214 (*.step)`.
2. Create new parts from the imported bodies if you need native features.
3. For the assembly, start a new assembly document and insert the imported parts, aligning them using the default origins. The `House_Assembly.step` file can also be imported directly if you simply need a quick visualization.

All dimensions are defined in millimetres. The house footprint is 8 m × 6 m with 3 m wall height and a 2 m tall gable roof.
