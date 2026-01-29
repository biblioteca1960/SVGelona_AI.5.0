"""
Run script for SVGelona_AI 5.0 with Language Bridge and Reasoning Core
Demonstrates initialization, flow, validation, and interactive reasoning over multiple domains.
"""

from engine.svgamma_engine import SVGammaEngine
from validation.falsifiability_tests import test_no_invariant_off_Lc
from validation.numerical_experiments import run_full_numerical_report
from language_bridge import LanguageBridge
from reasoning_core import ReasoningCore

# Example zeros (first few nontrivial zeros of zeta for demonstration)
zeros = [
    (0.5, 14.1347),
    (0.5, 21.0220),
    (0.5, 25.0109),
]

# Initialize engine
engine = SVGammaEngine(zeros)

# Run semi-spiral flow
engine.run_flow(dt=0.01, max_steps=5000)

# Initialize Language Bridge and Reasoning Core
bridge = LanguageBridge(engine)
reasoner = ReasoningCore(engine)

# Check invariants
all_invariant = engine.all_vectors_invariant()
print(f"All vectors invariant (on Lc): {all_invariant}")

# Falsifiability test
falsify_test = test_no_invariant_off_Lc(zeros)
print(f"Falsifiability test passed: {falsify_test}")

# Run numerical experiments
report = run_full_numerical_report(zeros)
print("Numerical Report:")
for key, value in report.items():
    print(f"{key}: {value}")

# --------------------------------------------------
# Interactive Language Bridge Queries
# --------------------------------------------------
language_queries = [
    "How many vectors are invariant?",
    "Show energies of all vectors",
    "Compute barycenter",
    "Generate report",
]

print("\n--- Language Bridge Queries ---")
for q in language_queries:
    print(f"> {q}")
    response = bridge.query(q)
    print(response)
    print('---')

# --------------------------------------------------
# Interactive Reasoning Core Queries
# --------------------------------------------------
reasoning_queries = [
    "How many vectors are invariant?",
    "Show energies of all vectors",
    "Compute barycenter",
    "Generate report",
    "What is the weather in Barcelona?",
    "Explain the semi-spiral flow",
    "Can you predict anything?"
]

print("\n--- Reasoning Core Queries ---")
for q in reasoning_queries:
    print(f"> {q}")
    response = reasoner.answer_query(q)
    print(response)
    print('---')
