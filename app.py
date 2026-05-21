import streamlit as st
import requests
prompt = st.chat_input("Enter your prompt")
if prompt:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json = {"prompt" : prompt}
    )

    st.write(response.json()["Response"])
    st.write(response.json()["Answer"])

