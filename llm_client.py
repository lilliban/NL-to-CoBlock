# va a definire i vari client LLM, per ora abbiamo GeminiClient, OpenAIClient, MockClient
from abc import ABC, abstractmethod


class LLMClient(ABC):
    """Classe base astratta — Strategy Pattern. Tutti i client devono implementare generate()."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Invia un prompt all'LLM e restituisce la risposta come stringa."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class GeminiClient(LLMClient):
    """
    Client per Google Gemini API (gratuito con piano base).
    Documentazione: ai.google.dev/gemini-api/docs
    API key: aistudio.google.com
    Installazione: pip install google-genai
    """

    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        self.api_key = api_key
        self.model = model
        from google import genai
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text.strip()


class OpenAIClient(LLMClient):
    """
    Client per OpenAI API (GPT-4o-mini, GPT-4o, ecc.)
    Documentazione: platform.openai.com/docs
    API key: platform.openai.com/api-keys
    Installazione: pip install openai
    """

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=api_key)
        except ImportError:
            raise ImportError("Esegui: pip install openai")

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()


class MockClient(LLMClient):
    """
    Client finto per testare il pipeline senza API key.
    Restituisce una regola CoBlock generica per qualsiasi input.
    Utile per verificare che il pipeline funzioni end-to-end.
    """

    def generate(self, prompt: str) -> str:
        return "createTX(function is CreateMarket) occ"