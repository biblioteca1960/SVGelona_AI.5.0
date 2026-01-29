"""
SVGelona_AI 5.0
dynamics/spiral_flow.py

Semi-spiral flow T₃⁻ for the SVG–Γ system.
Implements global descent along the Lyapunov energy,
respects the angular cone and critical line invariants.

Depends on:
- dynamics.angular_defect_dynamics
- axioms.angular_geometry
"""

import numpy as np
from dynamics.angular_defect_dynamics import descent_step, energy_of_embedding
from axioms.angular_geometry import is_on_critical_line, is_inside_svg_cone

# --------------------------------------------------
# Semi-Spiral Flow T₃⁻
# --------------------------------------------------

def semi_spiral_flow(z0: np.ndarray, dt: float = 0.01, max_steps: int = 10000) -> np.ndarray:
    """
    Integrates the semi-spiral flow:
        dz/dt = -∇E(z)
    while respecting the cone and energy invariants.

    Stops early if:
    - energy is numerically zero
    - vector is on critical line
    """
    z = np.copy(z0)

    for step in range(max_steps):
        E = energy_of_embedding(z)

        if is_on_critical_line(z) or E < 1e-12:
            break

        z_next = descent_step(z, dt)

        # enforce angular cone: reject step if leaves SVG cone
        if not (is_on_critical_line(z_next) or is_inside_svg_cone(z_next)):
            # Project back to admissible cone (simple clamping)
            z_next[2] = np.clip(z_next[2], -np.radians(38.7), np.radians(38.7))

        z = z_next

    return z


# --------------------------------------------------
# Flow Energy Trace
# --------------------------------------------------

def flow_energy_trace(z0: np.ndarray, dt: float = 0.01, max_steps: int = 10000) -> list[float]:
    """
    Returns the energy at each step along the semi-spiral flow.
    Useful for falsifiability tests and numerical validation.
    """
    z = np.copy(z0)
    energies = []

    for _ in range(max_steps):
        E = energy_of_embedding(z)
        energies.append(E)

        if E < 1e-12 or is_on_critical_line(z):
            break

        z_next = descent_step(z, dt)

        if not (is_on_critical_line(z_next) or is_inside_svg_cone(z_next)):
            z_next[2] = np.clip(z_next[2], -np.radians(38.7), np.radians(38.7))

        z = z_next

    return energies
