import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def buscar_informacion(tema: str) -> list:
    
    return "buscar informacion"