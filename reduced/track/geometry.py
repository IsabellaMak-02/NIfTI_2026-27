"""
Track construction: turns the rows described in a track preset into a
Collection of magnets.

This module was missing from the repository. It is reconstructed from the
inline loop in baseline_code.py's load_track_preset (lines 286-333), which
built the same magnets directly. If the original track/geometry.py turns
up, prefer it.
"""

from dataclasses import dataclass
from typing import Optional

import numpy as np

from geometry.collection import Collection
from geometry.shapes import PermMagnet, ElectroMagnet


@dataclass
class TrackRow:
    """
    One row of coils in a track preset. All lengths are in metres.
    x_position is the row's X coordinate; its n_coils coils are spaced
    `spacing` apart along Y, centred on y = 0. coil_type is "permanent"
    (uses magnetic_strength) or "electro" (uses turns).
    """

    row_index:         int
    x_position:        float
    n_coils:           int
    spacing:           float
    radius:            float
    height:            float
    coil_type:         str
    magnetic_strength: Optional[float] = None
    turns:             Optional[int]   = None


def track_rows_to_collection(rows):
    """
    Build the track Collection from a list of TrackRow. Coils sit at
    z = 0. Electromagnets start with zero current, as in the baseline;
    the currents are set later by track/control.py.
    """
    magnets = []

    for row in rows:
        # coil Y positions: n_coils spaced `spacing` apart, centred on 0
        y_offsets = (np.arange(row.n_coils) - (row.n_coils - 1) / 2) * row.spacing

        for y in y_offsets:
            position = np.array([row.x_position, y, 0.0])

            if row.coil_type == "permanent":
                magnets.append(PermMagnet(row.height, row.radius, position,
                                          row.magnetic_strength))
            elif row.coil_type == "electro":
                magnets.append(ElectroMagnet(row.height, row.radius, position,
                                             current=0.0, turns=row.turns))
            else:
                raise ValueError(
                    f"Unknown coil type '{row.coil_type}' in row {row.row_index}"
                )

    return Collection(magnets)
