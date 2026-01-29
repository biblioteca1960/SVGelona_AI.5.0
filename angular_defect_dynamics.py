"""
SVGelona_AI 5.0
dynamics/angular_defect_dynamics.py

Local angular-defect dynamics for the SVG–Γ system.
Implements the Lyapunov-compatible gradient structure
that underlies the T₃⁻ semi-spiral flow.

Depends ONLY on:
- axioms.energy_axioms
- axioms.angular_geometry
"""

import numpy as np
from axioms.energy_axioms import energy_of_embedding
from axioms.angular_geometry import embed_zero

# --------------------------------------------------
# Numerical Gradient of Energy
# --------------------------------------------------

def energy_gradient(z: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Numerical gradient ∇E(z) using central differences.
    Energy depends only on the angular component (z[2]),
    but the full gradient is defined for dynamical coherence.
    """
    grad = np.zeros_like(z, dtype=float)
    for i in range(len(z)):
        dz = np.zeros_like(z, dtype=float)
        dz[i] = eps
        grad[i] = (energy_of_embedding(z + dz) - energy_of_embedding(z - dz)) / (2.0 * eps)
    return grad


# --------------------------------------------------
# Local Descent Step
# --------------------------------------------------

def descent_step(z: np.ndarray, dt: float = 0.01) -> np.ndarray:
    """
    Single explicit Euler step for the negative gradient flow:

        z_{n+1} = z_n − dt · ∇E(z_n)

    This step strictly decreases energy unless z lies on Lc.
    """
    grad = energy_gradient(z)
    return z - dt * grad


# --------------------------------------------------
# Energy Monotonicity Check
# --------------------------------------------------

def energy_decreases(z: np.ndarray, dt: float = 0.01) -> bool:
    """
    Verifies Lyapunov monotonicity for one descent step.
    Returns True if energy(z_{n+1}) ≤ energy(z_n).
    """
    E0 = energy_of_embedding(z)
    z1 = descent_step(z, dt)
    E1 = energy_of_embedding(z1)
    return E1 <= E0 + 1e-12


# --------------------------------------------------
# Initialization Helper
# --------------------------------------------------

def initialize_from_zero(beta: float, gamma: float) -> np.ndarray:
    """
    Convenience function: embed a zeta zero
    and return its initial SVG–Γ state.
    """
    return embed_zero(beta, gamma)
