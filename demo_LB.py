"""
Language Bridge Demo for SVGelona_AI 5.0
Demonstrates interactive queries and narrative generation.
"""

from engine.svgamma_engine import SVGammaEngine
from language_bridge import LanguageBridge

# Example zeros
zeros = [
    (0.5, 14.1347),
    (0.5, 21.0220),
    (0.5, 25.0109),
]

# Initialize engine
engine = SVGammaEngine(zeros)

# Initialize Language Bridge
bridge = LanguageBridge(engine)

# Run flow briefly
engine.run_flow(dt=0.01, max_steps=500)

# Example queries
queries = [
    "How many vectors are invariant?",
    "Show energies of all vectors",
    "Compute barycenter",
    "Run flow",
    "Generate report",
]

for q in queries:
    print(f"> {q}")
    response = bridge.query(q)
    print(response)
    print('---')
