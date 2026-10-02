# Manifest: File Sources

Maps each file back to the original `baseline_code.py` (1,861 lines).

## Physics

| File | Source | Notes |
|------|--------|-------|
| `physics/field.py` | L746–892 | Elliptic-integral calculations, unchanged |
| `physics/field_query.py` | L701–724 | Renamed and refactored |
| `physics/ideal_field.py` | L725–745 | Unchanged |
| `physics/dipole.py` | L1132–1135, L1214, L1304, L1602 | Extracted to function |

## Geometry

| File | Source | Notes |
|------|--------|-------|
| `geometry/transforms.py` | L62 | Added `euler_from_matrix` for display |
| `geometry/collection.py` | L101–176 | Added `_build_body_inertia_tensor` |
| `geometry/shapes.py` | L177–285 | Geometry/material only |
| `geometry/sampling.py` | L1037–1108 | Unchanged |

## I/O

| File | Source | Notes |
|------|--------|-------|
| `data_io/presets.py` | L286–371 | Removed `input()` prompting |
| `data_io/sensor_data.py` | L372–383 | Unchanged |
| `data_io/field_data.py` | L384–669 | Unchanged |
| `data_io/results.py` | L670–700 | Renamed `savecurrents` to `save_currents` |

## Simulation

| File | Source | Notes |
|------|--------|-------|
| `simulation/dynamics.py` | L162–184, L1586–1751 | ODE split from plotting |
| `simulation/potential.py` | L1109–1370 | Extracted shared `_compute_grid()` |
| `simulation/sensor_check.py` | L893–1036 | Unchanged |

## Plotting

| File | Source | Notes |
|------|--------|-------|
| `plotting/geometry_plots.py` | L1371–1585 | Subset |
| `plotting/heatmaps.py` | L1371–1585 | Subset |
| `plotting/trajectory.py` | L1586–1751 | Extracted for reuse |

## UI

| File | Source | Notes |
|------|--------|-------|
| `track/control.py` | L25 | Extracted formula |
| `main.py` | L1752–1863 | Menu logic, options 1–5 |
| `config.py` | Scattered | Collected constants |

## Not Ported

- `control/` — Feedback controllers
- `geometry/quaternion.py` — Quaternion math
- `naming.py` — Run labeling
- `tests/` — Test suite
- `notebooks/` — Jupyter experiments
