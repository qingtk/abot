import requests
from .base import LLM

class OllamaClient(LLM):
    def generate(self, prompt):
        # r = requests.post(
        #     "http://localhost:11434/api/generate",
        #     json={"model": "llama3", "prompt": prompt}
        # )
        # return r.json()["response"]
        return "This is a placeholder for Ollama"