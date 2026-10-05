# The refactored code

This folder contains the ported code from baseline_code.py.does not include extensions/ feedback control/ SO(3) dynamics. This is verified againt original
## Glossary

**Physics:**
- `physics/field.py`: Elliptic-integral field calculations (numba-compiled)
- `physics/field_query.py` : Field evaluation at points
- `physics/ideal_field.py` : Analytic ideal fields for comparison
- `physics/dipole.py` : Dipole moment

**Geometry:**
- `geometry/transforms.py` : Rotation matrices (Euler angles)
- `geometry/collection.py` : Magnet assembly and inertia
- `geometry/shapes.py` : Magnet classes
- `geometry/sampling.py` : Pod point-cloud generation

**I/O:**
- `data_io/presets.py` : Load track and pod geometry
- `data_io/sensor_data.py` : Load sensor validation data
- `data_io/field_data.py` : Save/load computed field grids
- `data_io/results.py` : Save current assignments

**Simulation:**
- `simulation/dynamics.py` : Rigid-body ODE (open-loop)
- `simulation/potential.py` : Potential energy grids
- `simulation/sensor_check.py` : Validation against sensor data

**Plotting:**
- `plotting/geometry_plots.py` : 3D track and pod
- `plotting/heatmaps.py` : Potential energy heatmaps
- `plotting/trajectory.py` : Trajectory plots

**UI and config:**
- `track/control.py` : Current assignment formula
- `main.py` : Menu interface (options 1-5, open-loop only)
- `naming.py` : Run labeling
- `config.py` : Constants and paths

**Reference:**
- `baseline_code.py` : Original code (read-only)

## What I have removed from this handiver (found on other branches)

- `control/` : Feedback controllers
- `geometry/quaternion.py` : SO(3) utilities
- `simulation/calibration.py` : Self-calibration
- `simulation/closed_loop*.py` : Closed-loop simulation
- `tests/` : Test suite
- `notebooks/` : Jupyter notebooks

## Usage

```bash
python main.py
```
this will then call up the interactive menu

Menu options:
1. Plot Track and Pod in 3D
2. Check simulation against sensor data
3. Plot potential energy
4. Simulate pod movement (open-loop)
5. Compare controlled vs ideal field
6. Quit

```
reduced/
├── baseline_code.py # lewis' original code
├── config.py
├── main.py
├── naming.py
├── geometry/
│   ├── transforms.py
│   ├── collection.py
│   ├── shapes.py
│   └── sampling.py
├── data_io/
│   ├── presets.py
│   ├── sensor_data.py
│   ├── field_data.py
│   └── results.py
├── physics/
│   ├── field.py
│   ├── field_query.py
│   ├── ideal_field.py
│   └── dipole.py
├── simulation/
│   ├── dynamics.py
│   ├── potential.py
│   └── sensor_check.py
├── plotting/
│   ├── geometry_plots.py
│   ├── heatmaps.py
│   └── trajectory.py
├── track/
│   └── control.py
├── data/
└── README.md 
```

