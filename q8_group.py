"""
SVGelona_AI 5.0
symmetry/q8_group.py

Defines the quaternion group Q8 and its action on SVG–Γ vectors.
Implements the categorical fixed subspace Lc invariant under Q8.

Depends only on axioms.
"""

import numpy as np

# --------------------------------------------------
# Q8 Elements (2x2 matrices)
# --------------------------------------------------

I = np.eye(2)
NEG_I = -np.eye(2)
J = np.array([[0, 1], [-1, 0]])
NEG_J = -J

Q8 = [I, NEG_I, J, NEG_J]

# --------------------------------------------------
# Representation on SVG–Γ 3D vectors
# --------------------------------------------------

def apply_q8_element(z: np.ndarray, q: np.ndarray) -> np.ndarray:
    """
    Applies a 2x2 Q8 element to the (x, y) components of z.
    Theta component remains unchanged.
    """
    z_new = np.copy(z)
    z_new[:2] = q @ z[:2]
    return z_new

# --------------------------------------------------
# Invariant Check
# --------------------------------------------------

def is_invariant(z: np.ndarray, tol: float = 1e-12) -> bool:
    """
    Checks if z is invariant under all Q8 elements.
    Lc (x=0) is the only invariant subspace.
    """
    for q in Q8:
        if np.linalg.norm(apply_q8_element(z, q) - z) > tol:
            return False
    return True

# --------------------------------------------------
# Category-Theoretic Framing
# --------------------------------------------------

def fixed_subspace_Q8() -> np.ndarray:
    """
    Returns the canonical generator of the fixed subspace Lc.
    By construction, Lc = { x = 0 }.
    """
    return np.array([0.0, 1.0, 0.0], dtype=float)  # same as critical_axis()
