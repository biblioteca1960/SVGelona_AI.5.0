"""
SVGelona_AI 5.0
engine/state_manager.py

State manager for SVG–Γ engine.
Handles saving, loading, restoring, and checking global constraints.

Depends on:
- engine.svgamma_engine
- engine.global_constraints
"""

import pickle
from engine.global_constraints import check_global_constraints

# --------------------------------------------------
# Engine State Serialization
# --------------------------------------------------

def save_engine_state(engine, filename: str):
    """Serialize and save engine state to a file."""
    with open(filename, 'wb') as f:
        pickle.dump(engine, f)


def load_engine_state(filename: str):
    """Load serialized engine state from a file."""
    with open(filename, 'rb') as f:
        engine = pickle.load(f)
    return engine

# --------------------------------------------------
# Restore Engine to Valid State
# --------------------------------------------------

def restore_valid_engine_state(engine):
    """
    Projects all vectors onto global invariant subspace if constraints fail.
    Ensures engine consistency.
    """
    if not check_global_constraints(engine):
        engine.enforce_global_invariant()
    return engine
