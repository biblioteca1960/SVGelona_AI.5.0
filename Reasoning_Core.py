"""
SVGelona_AI 5.0 - Reasoning Core

Provides a general reasoning interface that can handle any user query,
combining the internal mathematical system (SVG–Γ) with natural language understanding.
"""

from engine.svgamma_engine import SVGammaEngine
from language_bridge import LanguageBridge
import requests

class ReasoningCore:
    def __init__(self, engine: SVGammaEngine):
        self.engine = engine
        self.bridge = LanguageBridge(engine)

    # --------------------------------------------------
    # General query processor
    # --------------------------------------------------
    def answer_query(self, question: str) -> str:
        question_lower = question.lower()

        # -------------------------
        # Check if it's a mathematical / internal query
        # -------------------------
        math_keywords = ['vector', 'energy', 'barycenter', 'invariant', 'flow', 'report']
        if any(word in question_lower for word in math_keywords):
            return self.bridge.query(question)

        # -------------------------
        # Check if it's weather related
        # -------------------------
        if 'weather' in question_lower or 'temperature' in question_lower or 'previsió' in question_lower:
            return self._weather_query(question)

        # -------------------------
        # Otherwise: default reasoning
        # -------------------------
        return self._default_reasoning(question)

    # --------------------------------------------------
    # Example weather API query
    # --------------------------------------------------
    def _weather_query(self, question: str) -> str:
        try:
            # extract city name (very simplified heuristic)
            tokens = question.split()
            city = tokens[-1]  # naive: last word

            # Example: use OpenWeatherMap API (pseudo-code, API key needed)
            api_key = 'YOUR_API_KEY'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
            response = requests.get(url).json()

            temp = response['main']['temp']
            desc = response['weather'][0]['description']
            return f"The current temperature in {city} is {temp}°C with {desc}."
        except Exception:
            return "Unable to fetch weather information. Please check the city name or API key."

    # --------------------------------------------------
    # Default reasoning for unknown domains
    # --------------------------------------------------
    def _default_reasoning(self, question: str) -> str:
        return f"I can reason about mathematics using SVG–Γ, or provide factual information if available. Your question was: '{question}'"
