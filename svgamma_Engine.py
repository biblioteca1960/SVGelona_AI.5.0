"""
SVGelona_AI 5.0
engine/svgamma_engine.py

Global SVG–Γ invariant engine.
Integrates axioms, dynamics, barycenter, and symmetries.

Depends on:
- axioms.bridge_theorems
- axioms.angular_geometry
- axioms.energy_axioms
- dynamics.angular_defect_dynamics
- dynamics.spiral_flow
- dynamics.barycenter
- symmetry.q8_group
- symmetry.mobius_action
- symmetry.invariants
"""

import numpy as np
from axioms.angular_geometry import embed_zero
from axioms.energy_axioms import energy_of_embedding
from dynamics.spiral_flow import semi_spiral_flow
from dynamics.barycenter import compute_barycenter, displacement_from_barycenter
from symmetry.invariants import check_global_invariant, project_to_global_invariant

# --------------------------------------------------
# Engine State Manager
# --------------------------------------------------

class SVGammaEngine:
    def __init__(self, zeros: list[tuple[float, float]]):
        # Initialize SVG–Γ vectors from list of (beta, gamma) zeros
        self.vectors = [embed_zero(beta, gamma) for beta, gamma in zeros]
        self.energies = [energy_of_embedding(z) for z in self.vectors]

    # --------------------------------------------------
    # Global Invariant Enforcement
    # --------------------------------------------------

    def enforce_global_invariant(self):
        self.vectors = [project_to_global_invariant(z) for z in self.vectors]
        self.energies = [energy_of_embedding(z) for z in self.vectors]

    # --------------------------------------------------
    # Run Semi-Spiral Flow on all vectors
    # --------------------------------------------------

    def run_flow(self, dt: float = 0.01, max_steps: int = 10000):
        for i, z in enumerate(self.vectors):
            z_new = semi_spiral_flow(z, dt=dt, max_steps=max_steps)
            self.vectors[i] = z_new
            self.energies[i] = energy_of_embedding(z_new)

    # --------------------------------------------------
    # Compute Barycenter and Displacements
    # --------------------------------------------------

    def global_barycenter(self) -> np.ndarray:
        return compute_barycenter(self.vectors)

    def barycenter_displacements(self) -> list[float]:
        bary = self.global_barycenter()
        return [displacement_from_barycenter(z, bary, e) for z, e in zip(self.vectors, self.energies)]

    # --------------------------------------------------
    # Check Engine Consistency
    # --------------------------------------------------

    def all_vectors_invariant(self) -> bool:
        return all(check_global_invariant(z) for z in self.vectors)
