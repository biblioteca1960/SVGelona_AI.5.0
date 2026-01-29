"""
SVGelona_AI 5.0 - Language Bridge v2

Provides a dynamic interface between SVG–Γ symbolic reasoning and natural language.
Allows queries, explanations, and narrative generation based on vectors, flows, energies, and invariants.
"""

from engine.svgamma_engine import SVGammaEngine
from validation.numerical_experiments import run_full_numerical_report
from symmetry.invariants import check_global_invariant

class LanguageBridge:
    def __init__(self, engine: SVGammaEngine):
        self.engine = engine

    # --------------------------------------------------
    # Explain individual vector in natural language
    # --------------------------------------------------
    def explain_vector(self, index: int) -> str:
        z = self.engine.vectors[index]
        E = self.engine.energies[index]
        invariant = check_global_invariant(z)
        desc = f"Vector {index} has coordinates {z}, energy {E:.5f}."
        if invariant:
            desc += " It lies on the critical line Lc and is invariant under Q8+Mobius."
        else:
            desc += " It is off the critical line and will flow towards Lc under T3-."
        return desc

    # --------------------------------------------------
    # Generate narrative report for all vectors
    # --------------------------------------------------
    def generate_report(self) -> str:
        report = []
        for i, z in enumerate(self.engine.vectors):
            report.append(self.explain_vector(i))
        return "\n".join(report)

    # --------------------------------------------------
    # Answer simple natural language queries
    # --------------------------------------------------
    def query(self, text: str) -> str:
        text = text.lower()
        if "invariant" in text or "critical line" in text:
            count = sum(check_global_invariant(z) for z in self.engine.vectors)
            return f"{count}/{len(self.engine.vectors)} vectors lie on the critical line Lc."
        elif "energy" in text:
            energies = [round(e,5) for e in self.engine.energies]
            return f"Energies of vectors: {energies}" 
        elif "barycenter" in text:
            from dynamics.barycenter import compute_barycenter
            bary = compute_barycenter(self.engine.vectors)
            return f"Barycenter of all vectors: {bary}" 
        elif "run flow" in text:
            self.engine.run_flow(dt=0.01, max_steps=1000)
            return "Flow applied for 1000 steps with dt=0.01. Vectors updated." 
        elif "report" in text:
            return self.generate_report()
        else:
            return "Query not recognized. Try asking about invariants, energy, barycenter, flow, or report."
