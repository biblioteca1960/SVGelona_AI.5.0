"""
SVGelona_AI 5.0
symmetry/mobius_action.py

Implements Möbius transformations on SVG–Γ vectors.
Ensures compatibility with Q8 invariance and Lc.

Depends on:
- symmetry.q8_group
- axioms.angular_geometry
"""

import numpy as np
from symmetry.q8_group import apply_q8_element, Q8
from axioms.angular_geometry import embed_zero, critical_axis

# --------------------------------------------------
# Möbius Action on 2D Components
# --------------------------------------------------

def mobius_action(z: np.ndarray, a: complex, b: complex, c: complex, d: complex) -> np.ndarray:
    """
    Applies Möbius transformation on (x, y) components of z:
        w = (a z + b) / (c z + d)
    Theta component remains unchanged.
    """
    z_new = np.copy(z)
    x, y = z[:2]
    z_complex = complex(x, y)
    denom = c * z_complex + d
    if denom == 0:
        raise ZeroDivisionError("Möbius transformation singular")
    w = (a * z_complex + b) / denom
    z_new[0] = w.real
    z_new[1] = w.imag
    return z_new

# --------------------------------------------------
# Compatibility with Q8
# --------------------------------------------------

def mobius_commutes_with_q8(z: np.ndarray, a, b, c, d) -> bool:
    """
    Checks that applying Möbius then Q8 is equivalent to
    Q8 then Möbius on the vector z.
    """
    for q in Q8:
        z1 = apply_q8_element(mobius_action(z, a, b, c, d), q)
        z2 = mobius_action(apply_q8_element(z, q), a, b, c, d)
        if np.linalg.norm(z1 - z2) > 1e-12:
            return False
    return True

# --------------------------------------------------
# Projection to Lc
# --------------------------------------------------

def project_to_Lc(z: np.ndarray) -> np.ndarray:
    """
    Projects a vector onto the critical line Lc (x=0).
    """
    z_proj = np.copy(z)
    z_proj[0] = 0.0
    return z_proj
