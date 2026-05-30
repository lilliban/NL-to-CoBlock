import os
from rule_generator import RuleGenerator
from llm_factory import LLMFactory

PROVIDER = "gemini"
#se lo volete fa parti dovete mette la vostra chiave al posto dei puntini
API_KEY = os.getenv("GEMINI_API_KEY", "..........")
MODEL = "gemini-2.5-flash"

#frasi nel linguaggio naturale
REQUIREMENTS = [
    # CR3
    "The initial reporter must get properly rewarded",
    # CR6
    "The end betting event date must not be earlier than the market creation date",
    # CR7
    "The creation bond is returned to the market creator only if the designated reporter reports within 24 hours after the market end time",
]


if __name__ == "__main__":

    client = LLMFactory.create(PROVIDER, api_key=API_KEY, model=MODEL)
    generator = RuleGenerator(client)

    print(f"Provider: {client}")


    for frase in REQUIREMENTS:
        print(f"\nInput:  {frase}")
        print(f"Output:")
        risultato = generator.generate(frase)
        print(risultato)
        print("-" * 60)
