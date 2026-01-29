"""
Reasoning Core Demo for SVGelona_AI 5.0
Demonstrates interactive queries over mathematical and external domains.
"""

from engine.svgamma_engine import SVGammaEngine
from reasoning_core import ReasoningCore

# Example zeros
zeros = [
    (0.5, 14.1347),
    (0.5, 21.0220),
    (0.5, 25.0109),
]

# Initialize engine
engine = SVGammaEngine(zeros)

# Run flow briefly
engine.run_flow(dt=0.01, max_steps=500)

# Initialize Reasoning Core
reasoner = ReasoningCore(engine)

# Example interactive queries
queries = [
    "How many vectors are invariant?",
    "Show energies of all vectors",
    "Compute barycenter",
    "Generate report",
    "What is the weather in Barcelona?",
    "Explain the semi-spiral flow",
    "Can you predict anything?"
]

for q in queries:
    print(f"> {q}")
    response = reasoner.answer_query(q)
    print(response)
    print('---')
