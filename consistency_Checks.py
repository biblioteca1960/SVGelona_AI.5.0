"""
SVGelona_AI 5.0
validation/consistency_checks.py

Symbolic and structural consistency checks for SVG–Γ system.
Ensures axioms, dynamics, flow, and symmetries are coherent.

Depends on:
- engine.svgamma_engine
- dynamics.angular_defect_dynamics
- symmetry.invariants
"""

from engine.svgamma_engine import SVGammaEngine
from dynamics.angular_defect_dynamics import energy_of_embedding
from symmetry.invariants import check_global_invariant

# --------------------------------------------------
# Check Axioms vs Energy
# --------------------------------------------------

def check_axiom_energy_consistency(engine: SVGammaEngine) -> bool:
    """
    Verifies that all vectors satisfy energy axioms.
    - Lc vectors: zero energy
    - Off Lc: strictly positive energy
    """
    for z in engine.vectors:
        E = energy_of_embedding(z)
        invariant = check_global_invariant(z)
        if invariant and E > 1e-12:
            return False
        if not invariant and E < 1e-12:
            return False
    return True

# --------------------------------------------------
# Check No Circularity in Flow
# --------------------------------------------------

def check_flow_non_circular(engine: SVGammaEngine, steps: int = 10, dt: float = 0.01) -> bool:
    """
    Ensures that iterating semi-spiral flow does not return vectors to previous states.
    Simple hash-based check.
    """
    from dynamics.spiral_flow import semi_spiral_flow
    seen = set()
    for z in engine.vectors:
        z_curr = z.copy()
        for _ in range(steps):
            z_curr = semi_spiral_flow(z_curr, dt=dt, max_steps=1)
            # hash by rounding to 12 decimals
            h = tuple(round(x, 12) for x in z_curr)
            if h in seen:
                return False
            seen.add(h)
    return True
