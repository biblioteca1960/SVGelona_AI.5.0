"""
SVGelona_AI 5.0
axioms/angular_geometry.py

Pure geometric layer of the SVG–Γ system.
Defines vector spaces, cones, critical axis, and embeddings.

This module depends ONLY on axioms.bridge_theorems.
"""

import math
import numpy as np
from axioms.bridge_theorems import CRITICAL_BETA, angular_deviation

# --------------------------------------------------
# SVG–Γ Vector Space
# --------------------------------------------------

# We work in R^3 with coordinates:
#   z = (x, y, theta)
# where:
#   x = beta - 1/2  (critical deviation)
#   y = gamma       (imaginary height)
#   theta = angular deviation


def embed_zero(beta: float, gamma: float) -> np.ndarray:
    """
    Embeds a zeta zero rho = beta + i gamma
    into the SVG–Γ vector space.
    """
    theta = angular_deviation(beta, gamma)
    return np.array([
        beta - CRITICAL_BETA,
        gamma,
        theta
    ], dtype=float)


# --------------------------------------------------
# Critical Line and Axis
# --------------------------------------------------


def is_on_critical_line(z: np.ndarray, tol: float = 1e-12) -> bool:
    """
    Checks whether a vector lies on the critical line Lc.
    In SVG–Γ: Lc = { x = 0 }.
    """
    return abs(z[0]) < tol


def critical_axis() -> np.ndarray:
    """
    Returns the unit vector along the critical axis.
    """
    return np.array([0.0, 1.0, 0.0], dtype=float)


# --------------------------------------------------
# Angular Cone Geometry (Bridge-Theorem 3)
# --------------------------------------------------

ALPHA_MAX_DEGREES = 38.7
ALPHA_MAX = math.radians(ALPHA_MAX_DEGREES)


def angle_with_critical_axis(z: np.ndarray) -> float:
    """
    Returns the angle between vector z and the critical axis.
    """
    axis = critical_axis()
    norm_z = np.linalg.norm(z)
    if norm_z == 0:
        return 0.0
    cos_angle = np.dot(z, axis) / norm_z
    cos_angle = max(min(cos_angle, 1.0), -1.0)
    return math.acos(cos_angle)


def is_inside_svg_cone(z: np.ndarray) -> bool:
    """
    Checks whether z lies inside the SVG–Γ admissible cone.
    This cone enforces the 0.78 non-cancellation bound.
    """
    return angle_with_critical_axis(z) <= ALPHA_MAX


# --------------------------------------------------
# Geometric Invariants
# --------------------------------------------------


def cone_cosine_lower_bound() -> float:
    """
    Returns cos(alpha_max), the structural non-cancellation constant.
    """
    return math.cos(ALPHA_MAX)


# --------------------------------------------------
# Consistency Checks
# --------------------------------------------------


def check_geometric_consistency(beta: float, gamma: float) -> bool:
    """
    A zero is geometrically admissible iff its embedding
    lies inside the SVG–Γ cone or on the critical line.
    """
    z = embed_zero(beta, gamma)
    return is_on_critical_line(z) or is_inside_svg_cone(z)
