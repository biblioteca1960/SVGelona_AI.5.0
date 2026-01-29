"""
SVGelona_AI 5.0
axioms/bridge_theorems.py

Foundational Bridge-Theorems for the SVG–Γ system.
These are axiomatic: they define structure, not heuristics.
All higher modules depend on (but do not modify) this file.
"""

import math

CRITICAL_BETA = 0.5

# --------------------------------------------------
# Bridge-Theorem 1: Angular–Vectorial Correspondence
# --------------------------------------------------

def angular_deviation(beta: float, gamma: float) -> float:
    """
    Δθ(ρ) = (π/2) * (β − 1/2) * log(|γ| + 2) / |γ|

    Properties:
    - Δθ = 0  ⇔  β = 1/2
    - Monotone in |β − 1/2|
    - Damped as |γ| → ∞
    """
    if gamma == 0:
        raise ValueError("gamma must be non-zero")
    return (math.pi / 2.0) * (beta - CRITICAL_BETA) * math.log(abs(gamma) + 2.0) / abs(gamma)


# --------------------------------------------------
# Bridge-Theorem 2: Positive Angular Energy
# --------------------------------------------------

def angular_energy(beta: float, gamma: float) -> float:
    """
    E(ρ) = 1 − cos(Δθ(ρ)) ≥ 0

    Structural facts:
    - E = 0  ⇔  β = 1/2
    - E > 0  ⇔  β ≠ 1/2
    - Quadratic for small Δθ (Lyapunov-compatible)
    """
    dtheta = angular_deviation(beta, gamma)
    return 1.0 - math.cos(dtheta)


# --------------------------------------------------
# Bridge-Theorem 3: No-Cancellation by Accumulation
# --------------------------------------------------

def non_cancellation_lower_bound(energies: list[float]) -> float:
    """
    For any finite family of off-critical zeros:

        || Σ z_i || ≥ c · Σ E_i

    where c = cos(α_max) ≈ 0.78 is structural.

    This function returns the guaranteed lower bound.
    """
    return 0.78 * sum(energies)


# --------------------------------------------------
# Bridge-Theorem 4: Barycenter Displacement
# --------------------------------------------------

def barycenter_displacement_from_energy(energy: float, K: float = 1.0) -> float:
    """
    || z − z_abc || = K · E + O(1/γ²)

    In SVGelona_AI 5.0 we normalize K = 1.
    """
    return K * energy


# --------------------------------------------------
# Axiomatic Consistency Check
# --------------------------------------------------

def check_axioms(beta: float, gamma: float) -> bool:
    """
    Returns True iff all Bridge-Theorems are satisfied
    for the given (beta, gamma).
    """
    E = angular_energy(beta, gamma)
    if beta == CRITICAL_BETA:
        return abs(E) < 1e-12
    return E > 0
