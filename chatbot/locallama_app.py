from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st 
import os
from dotenv import Load_dotenv
Load_dotenv()

os.environ['LANGCHAIN_TRACKING_V2']='true'
os.environ['Langchain_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("System","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit Framework

st.title("Langchain Demo with Ollama LLM")
input_text=st.text_input("Enter your queries here")

# Ollama LLM
llm=Ollama(model="llama3:8b",temperature=0.9)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))