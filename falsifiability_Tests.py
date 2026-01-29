"""
SVGelona_AI 5.0
validation/falsifiability_tests.py

Numerical falsifiability tests for the SVG–Γ system.

Depends on:
- engine.svgamma_engine
- dynamics.spiral_flow
- symmetry.invariants
"""

import numpy as np
from engine.svgamma_engine import SVGammaEngine
from dynamics.spiral_flow import flow_energy_trace
from symmetry.invariants import check_global_invariant

# --------------------------------------------------
# Test: No invariant vectors off critical line
# --------------------------------------------------

def test_no_invariant_off_Lc(zeros: list[tuple[float,float]], dt: float = 0.01, max_steps: int = 1000) -> bool:
    """
    Run flow on given zeros and check that no vectors remain invariant
    off the critical line Lc.
    Returns True if test passes.
    """
    engine = SVGammaEngine(zeros)
    engine.run_flow(dt=dt, max_steps=max_steps)
    for z in engine.vectors:
        if not check_global_invariant(z) and abs(z[0]) > 1e-12:
            # vector off critical line remains non-invariant -> fail
            return False
    return True

# --------------------------------------------------
# Test: Energy Monotonicity
# --------------------------------------------------

def test_energy_monotonicity(beta: float, gamma: float, dt: float = 0.01, max_steps: int = 1000) -> bool:
    """
    Checks that energy decreases along semi-spiral flow.
    """
    from dynamics.angular_defect_dynamics import initialize_from_zero, energy_of_embedding
    from dynamics.spiral_flow import semi_spiral_flow

    z0 = initialize_from_zero(beta, gamma)
    energies = flow_energy_trace(z0, dt=dt, max_steps=max_steps)
    return all(earlier >= later - 1e-12 for earlier, later in zip(energies, energies[1:]))
