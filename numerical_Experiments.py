"""
SVGelona_AI 5.0
validation/numerical_experiments.py

Numerical experiments for SVG–Γ system.
Generates energy trajectories, barycenter displacements, and invariant checks.

Depends on:
- engine.svgamma_engine
- dynamics.spiral_flow
- dynamics.barycenter
- symmetry.invariants
- validation.falsifiability_tests
"""

import numpy as np
from engine.svgamma_engine import SVGammaEngine
from dynamics.spiral_flow import flow_energy_trace
from dynamics.barycenter import compute_barycenter, displacement_from_barycenter
from symmetry.invariants import check_global_invariant

# --------------------------------------------------
# Experiment: Energy Trace for a Single Zero
# --------------------------------------------------

def experiment_energy_trace(beta: float, gamma: float, dt: float = 0.01, max_steps: int = 1000) -> list[float]:
    engine = SVGammaEngine([(beta, gamma)])
    z0 = engine.vectors[0]
    return flow_energy_trace(z0, dt=dt, max_steps=max_steps)

# --------------------------------------------------
# Experiment: Barycenter Displacements for Multiple Zeros
# --------------------------------------------------

def experiment_barycenter_displacements(zeros: list[tuple[float,float]], dt: float = 0.01, max_steps: int = 1000) -> list[float]:
    engine = SVGammaEngine(zeros)
    engine.run_flow(dt=dt, max_steps=max_steps)
    return engine.barycenter_displacements()

# --------------------------------------------------
# Experiment: Invariant Fraction
# --------------------------------------------------

def experiment_invariant_fraction(zeros: list[tuple[float,float]], dt: float = 0.01, max_steps: int = 1000) -> float:
    engine = SVGammaEngine(zeros)
    engine.run_flow(dt=dt, max_steps=max_steps)
    count_invariant = sum(check_global_invariant(z) for z in engine.vectors)
    return count_invariant / len(engine.vectors) if engine.vectors else 0.0

# --------------------------------------------------
# Combined Experiment Report
# --------------------------------------------------

def run_full_numerical_report(zeros: list[tuple[float,float]], dt: float = 0.01, max_steps: int = 1000) -> dict:
    return {
        'energy_traces': [experiment_energy_trace(beta, gamma, dt, max_steps) for beta, gamma in zeros],
        'barycenter_displacements': experiment_barycenter_displacements(zeros, dt, max_steps),
        'invariant_fraction': experiment_invariant_fraction(zeros, dt, max_steps)
    }
