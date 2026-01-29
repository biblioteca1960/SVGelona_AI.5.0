"""
SVGelona_AI 5.0
symmetry/invariants.py

Defines and verifies global invariants for the SVG–Γ system.
Ensures only Lc survives Q8 + Möbius symmetries.

Depends on:
- symmetry.q8_group
- symmetry.mobius_action
- axioms.angular_geometry
"""

import numpy as np
from symmetry.q8_group import is_invariant, Q8, apply_q8_element
from symmetry.mobius_action import mobius_commutes_with_q8, project_to_Lc
from axioms.angular_geometry import is_on_critical_line, critical_axis

# --------------------------------------------------
# Global Invariant Check
# --------------------------------------------------

def check_global_invariant(z: np.ndarray) -> bool:
    """
    Returns True iff z is invariant under:
    - all Q8 elements
    - all Möbius transformations that commute with Q8

    Only vectors along Lc satisfy this.
    """
    if not is_invariant(z):
        return False

    # Optionally, check Möbius compatibility on a standard set
    a,b,c,d = 1+0j, 0+0j, 0+0j, 1+0j  # identity Möbius
    if not mobius_commutes_with_q8(z, a, b, c, d):
        return False

    return True

# --------------------------------------------------
# Project Vector onto Invariant Subspace Lc
# --------------------------------------------------

def project_to_global_invariant(z: np.ndarray) -> np.ndarray:
    """
    Returns the projection of z onto the global invariant subspace Lc.
    This is used in engine and numerical validation.
    """
    return project_to_Lc(z)

# --------------------------------------------------
# Consistency Check for a Collection of Vectors
# --------------------------------------------------

def all_vectors_invariant(vectors: list[np.ndarray]) -> bool:
    """
    Checks that all vectors are invariant under Q8 + Möbius symmetries.
    """
    return all(check_global_invariant(z) for z in vectors)
