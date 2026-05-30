from prompt_builder import PromptBuilder
#controller
class RuleGenerator:

    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.builder = PromptBuilder()

    def generate(self, frase_utente):
        # 1. costruisci il prompt
        prompt = self.builder.build(frase_utente)
        # 2. manda il prompt all'LLM
        risposta = self.llm_client.generate(prompt)
        # 3. restituisci la risposta
        return risposta


