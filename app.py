from fastapi import FastAPI
from brain.router import execute
from brain.learning import daily_learning
from models.ollama_client import OllamaClient

app = FastAPI()
llm = OllamaClient()

@app.get("/run/{skill}")
def run(skill: str, text: str = None):
    if text:
        return {"result": execute(skill, text)}
    else:
        return {"result": execute(skill)}

@app.get("/learn")
def learn():
    return {"learning": daily_learning(llm)}