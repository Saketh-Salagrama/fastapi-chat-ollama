from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time, asyncio
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
app = FastAPI()
class Prompt(BaseModel):
    prompt: str
async def generator(prompt):
    yield "Thinking....\n"
    await asyncio.sleep(1)
    x = llm.invoke(prompt)
    yield x
@app.post("/chat")
async def chat_llm(payload: Prompt):
    return StreamingResponse(generator(payload.prompt), media_type="text/plain")