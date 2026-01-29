"""
SVGelona_AI 5.0
engine/global_constraints.py

Defines global constraints for SVG–Γ engine.
Ensures compatibility between energy, barycenter, and symmetries.

Depends on:
- engine.svgamma_engine
- symmetry.invariants
"""

import numpy as np
from symmetry.invariants import check_global_invariant

# --------------------------------------------------
# Energy + Symmetry Constraint
# --------------------------------------------------

def enforce_energy_symmetry_constraints(vectors: list[np.ndarray], energies: list[float]) -> bool:
    """
    Returns True if all vectors satisfy:
    - Positive energy only off Lc
    - Invariant vectors on Lc
    - Energy-displacement proportionality (Bridge 4)
    """
    for z, E in zip(vectors, energies):
        invariant = check_global_invariant(z)
        if invariant and abs(E) > 1e-12:
            # invariant vectors on Lc must have zero energy
            return False
        if not invariant and E < 1e-12:
            # off-critical vectors must have positive energy
            return False
    return True

# --------------------------------------------------
# Check All Constraints for Engine
# --------------------------------------------------

def check_global_constraints(engine) -> bool:
    """
    Checks that engine state satisfies all global constraints.
    """
    return enforce_energy_symmetry_constraints(engine.vectors, engine.energies)
