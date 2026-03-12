from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import openai
import streamlit as st
import os
from dotenv import load_dotenv


os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("System","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit Framework

st.title("Langchain Demo Streamlit App")
input_text=st.text_input("Enter your queries here")

# OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.9)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))

