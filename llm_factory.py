# va a creare il client giusto, questo viene usato poi dal main

from llm_client import GeminiClient, OpenAIClient, MockClient


class LLMFactory:

    @staticmethod
    def create(provider: str, api_key: str = "", model: str = ""):
        """
       provider è il provider da usare, quindi gemini openai o mock
       api_key è la API key del provider scelto
       model è il modello da usare

       Va a ritornare il client pronto all'uso
        """
        if provider == "gemini":
            return GeminiClient(api_key=api_key, model=model or "gemini-2.5-flash")

        elif provider == "openai":
            return OpenAIClient(api_key=api_key, model=model or "gpt-4o-mini")

        elif provider == "mock":
            return MockClient()

        else:
            raise ValueError(
                f"Provider '{provider}' non riconosciuto. "
                f"Usa: 'gemini', 'openai', o 'mock'."
            )