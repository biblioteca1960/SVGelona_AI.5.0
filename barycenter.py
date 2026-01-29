"""
SVGelona_AI 5.0
dynamics/barycenter.py

Computes barycenter and energy-proportional displacement
for SVG–Γ vectors, implementing Bridge-Theorem 4.

Depends on:
- axioms.bridge_theorems
- dynamics.angular_defect_dynamics
"""

import numpy as np
from axioms.bridge_theorems import barycenter_displacement_from_energy

# --------------------------------------------------
# Barycenter Computation
# --------------------------------------------------

def compute_barycenter(vectors: list[np.ndarray]) -> np.ndarray:
    """
    Returns the hyperbolic barycenter (componentwise average) of a set of vectors.
    """
    if len(vectors) == 0:
        raise ValueError("Vector list must be non-empty")
    return np.mean(np.stack(vectors), axis=0)

# --------------------------------------------------
# Displacement Relative to Barycenter
# --------------------------------------------------

def displacement_from_barycenter(z: np.ndarray, barycenter: np.ndarray, energy: float, K: float = 1.0) -> float:
    """
    Computes || z - z_abc || as per Bridge-Theorem 4:
        || z - z_abc || ≈ K * E + O(1/gamma^2)

    Here we normalize K = 1 by default.
    """
    diff = z - barycenter
    norm_diff = np.linalg.norm(diff)
    return max(norm_diff, barycenter_displacement_from_energy(energy, K))

# --------------------------------------------------
# Energy-Weighted Barycenter
# --------------------------------------------------

def energy_weighted_barycenter(vectors: list[np.ndarray], energies: list[float]) -> np.ndarray:
    """
    Returns the barycenter weighted by angular energies.
    Ensures vectors with higher energy pull more strongly.
    """
    if len(vectors) != len(energies):
        raise ValueError("Vectors and energies must have same length")
    weighted = np.sum([v*e for v,e in zip(vectors, energies)], axis=0)
    total_energy = sum(energies)
    if total_energy == 0:
        return compute_barycenter(vectors)
    return weighted / total_energy
