import requests
import streamlit as st


def get_openai_response(input_text: str):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}}
    )
    return response.json()['output']['content']


st.title("Chatbot with OpenAI API")
input_text = st.text_input("What topic do you want an essay on?")

if input_text:
    st.write(get_openai_response(input_text))