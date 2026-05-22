import streamlit as st
import requests
prompt = st.chat_input("Enter your prompt")
if prompt:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json = {"prompt" : prompt},
        stream=True
    )
#Streaming the front end side Here wee recieve the chunks frm backend
    total_answer = ""
    display = st.empty()
    for chunk in response.iter_content(chunk_size=1):
        if chunk:
            text = chunk.decode("utf-8")
            total_answer += text
            display.markdown(total_answer)

