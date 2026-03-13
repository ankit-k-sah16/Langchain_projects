from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A server for Langchain LLMs"

)

#OpenAI model instance
model=ChatOpenAI()
##ollama llama3:8b model instance 
llm=Ollama(model="llama3:8b")

#Prompt Templates
prompt1=ChatPromptTemplate.from_template("Write an advertisement for {product} with 50 words")

prompt2=ChatPromptTemplate.from_template("Write an promotion script for {product} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/openai-advertisement"
)

add_routes(
    app,
    prompt2|llm,
    path="/ollama-promotion"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)