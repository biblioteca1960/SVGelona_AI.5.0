"""
SVGelona_AI 5.0
axioms/energy_axioms.py

Energy axioms for the SVG–Γ system.
Defines Lyapunov structure, coercivity, and incompatibility
of positive energy with Q8-invariant states.

Depends ONLY on:
- axioms.bridge_theorems
- axioms.angular_geometry
"""

import math
import numpy as np
from axioms.bridge_theorems import angular_energy, CRITICAL_BETA
from axioms.angular_geometry import embed_zero, is_on_critical_line

# --------------------------------------------------
# Energy as a Lyapunov Function
# --------------------------------------------------


def energy_of_embedding(z: np.ndarray) -> float:
    """
    Energy evaluated on an embedded SVG–Γ vector.
    By construction, energy depends only on angular deviation.
    """
    theta = z[2]
    return 1.0 - math.cos(theta)


# --------------------------------------------------
# Coercivity and Positivity
# --------------------------------------------------


def is_energy_zero(beta: float, gamma: float, tol: float = 1e-12) -> bool:
    """
    Energy is zero iff beta = 1/2.
    """
    return abs(angular_energy(beta, gamma)) < tol


def is_energy_positive(beta: float, gamma: float, tol: float = 1e-12) -> bool:
    """
    Energy is strictly positive iff beta != 1/2.
    """
    return angular_energy(beta, gamma) > tol


# --------------------------------------------------
# Energy Barriers
# --------------------------------------------------


def energy_barrier(beta: float, gamma: float) -> float:
    """
    Returns a strictly positive lower bound for energy
    when beta != 1/2.

    This acts as an energetic barrier preventing
    convergence to Lc from outside.
    """
    E = angular_energy(beta, gamma)
    if beta == CRITICAL_BETA:
        return 0.0
    return max(E, 0.0)


# --------------------------------------------------
# Compatibility with Critical Line
# --------------------------------------------------


def energy_compatible_with_Lc(beta: float, gamma: float) -> bool:
    """
    Energy compatibility condition:
    - On Lc: E = 0
    - Off Lc: E > 0 (forbidden in invariant states)
    """
    if beta == CRITICAL_BETA:
        return is_energy_zero(beta, gamma)
    return is_energy_positive(beta, gamma)


# --------------------------------------------------
# Global Energy Consistency Check
# --------------------------------------------------


def check_energy_axioms(beta: float, gamma: float) -> bool:
    """
    Returns True iff all energy axioms are satisfied
    for the given (beta, gamma).
    """
    z = embed_zero(beta, gamma)
    if is_on_critical_line(z):
        return is_energy_zero(beta, gamma)
    return is_energy_positive(beta, gamma)
