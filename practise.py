from fastapi import FastAPI, Body
from pydantic import BaseModel
#import streamlit as st
app = FastAPI()
class Post(BaseModel):
    Q: str
    A: str
@app.get("/")
async def root():
    return {"message" : "My first Backend Program"}
@app.get("/login")
async def login_user():
    #x = st.chat_input("Enter Your name")
    return {f"User" : "Name"}

@app.post("/chat")
async def get_input(payload: Post):
    print(payload.Q)
    return {"Input" : "payload"}
#I need an input (prompt) from user(browser)

