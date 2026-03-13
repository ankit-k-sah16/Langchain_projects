import requests 
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/openai-advertisement/invoke", json={"input": {'topic': input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/ollama-promotion/invoke",
        json={"input": {"product": input_text}}
    )
    return response.json()["output"]

st.title("Langchain Demo with FastAPI Client ")
input_text=st.text_input("Enter your topic for advertisement here")
input_text2=st.text_input("Enter your topic for promotion here")

if input_text:
    st.write(get_openai_response(input_text))

if input_text2:
    st.write(get_ollama_response(input_text2))