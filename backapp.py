from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
app = FastAPI()
class Prompt(BaseModel):
    prompt: str
@app.get("/")
def login():
    return {"User":"User_login"}
@app.post("/chat")
async def chat_llm(payload: Prompt):
    x = llm.invoke(payload.prompt)
    return {"Response":f"You have asked for {payload.prompt}",
            "Answer" : f"Answer is {x}"}