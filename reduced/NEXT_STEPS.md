# Extending the Baseline

This folder is the clean baseline. To add features safely after understanding the core, here are the best places to build:

## Safe Extensions

**1. New plotting functions**
- Where: `plotting/`
- Pattern: Add a new file or function in existing files
- Example: `plotting/custom_heatmap.py`

**2. New analysis modes**
- Where: `simulation/sensor_check.py` or new `simulation/analysis.py`
- Pattern: Post-process or analyze existing outputs
- Example: RMS error, stability metrics

**3. Potential energy variants**
- Where: `simulation/potential.py`
- Pattern: Add `energy_potential_custom()` alongside the existing three
- Example: Hybrid static/controlled mode

**4. New geometry presets**
- Where: `data/Presets/` (Excel files)
- Steps: Copy an existing preset, modify coil positions/currents, run parity check, test

**5. Menu improvements**
- Where: `main.py`
- Pattern: Add new options that call existing or new analysis functions
- Example: Option 6 for batch analysis or parameter sweep

## Risky Extensions (Skip These)

**Feedback control**
- Requires tuning, stability analysis, full re-testing. Build in `control/` folder separately if needed.

**Physics kernels**
- Field kernels are parity-checked. Fork to `physics/field_custom.py` if needed, but test in isolation first.

**Dipole model**
- Single-point dipole is baked into potential calculations. Use the multi-dipole version in the main package instead.

**Attitude representation**
- Euler angles couple to the ODE. Quaternion version exists in the main package if needed.

## Testing Checklist

Before deploying an extension:

1. Run parity check (if you touched physics):
   ```bash
   cd ..
   python notebooks/nblib/parity_check.py
   ```

2. Test against sensor data (if you touched field or potential):
   - main.py > option 2 > "Check simulation against sensor data"

3. Verify open-loop dynamics (any changes):
   - main.py > option 4 > "Simulate pod movement"
   - Should be smooth and stable

4. Document: add docstrings, update this file, cite sources

## Risk Levels

| Folder | Risk | Notes |
|--------|------|-------|
| `physics/` | Critical | Parity check must pass |
| `simulation/` | High | Must validate against sensor data |
| `plotting/` | Low | Safe to add freely |
| `geometry/` | Medium | Affects inertia, rotation, transforms |
| `data_io/` | Low | Just I/O |
| `config.py` | Medium | Values cascade downstream |
| `main.py` | Low | UI is isolated |

## Quick Extension: Parameter Sweep

Run dynamics across a 2D grid of initial conditions:

1. Create `simulation/parameter_sweep.py`
2. Loop over initial states, call `run_dynamics()` each time
3. Aggregate results (max height, final position, stability)
4. Visualize in `plotting/sweep_heatmap.py`

Estimated: 2–3 hours. Safe because it only calls tested functions.
