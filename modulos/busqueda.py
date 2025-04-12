import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_TOKEN")
TAVILY_KEY = os.getenv("TAVILY_API_KEY")

def parsear_resultado(respuesta: str):
    """Intenta extraer JSON de la respuesta del agente, si falla usa Tavily directamente"""
    try:
        # Busca el JSON dentro del texto (el agente a veces añade comentarios)
        inicio = respuesta.find('[')
        fin = respuesta.rfind(']') + 1
        json_str = respuesta[inicio:fin]
        return json.loads(json_str)
    except:
        return None

def buscar_informacion(tema: str):
    # 1. Configurar Tavily como respaldo
    tavily_tool = TavilySearchResults(api_key=TAVILY_KEY, max_results=5)
    
    # 2. Herramientas para el agente
    tools = [Tool(
        name="Busqueda_Web",
        func=tavily_tool.run,
        description="Busca en web. Devuelve título, contenido y URL."
    )]

    # 3. Prompt MÁS ESTRICTO
    prompt_template = PromptTemplate.from_template("""
    Eres un asistente que SOLO devuelve JSON. Busca sobre: {topic}
    
    REGLAS:
    1. Usa 'Busqueda_Web' y devuelve ESTE FORMATO:
    ```json
    [
        {{
            "titulo": "Título exacto del resultado",
            "contenido": "3-4 frases clave",
            "enlace": "URL_completa"
        }}
    ]
    ```
    2. ¡NUNCA inventes datos! Si no hay resultados, devuelve [].
    """)

    # 4. Configurar agente
    llm = ChatOpenAI(model="gpt-4-turbo", temperature=0, api_key=OPENAI_KEY)
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
    executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)

    try:
        # 5. Ejecutar agente
        respuesta = executor.invoke({"input": prompt_template.format(topic=tema)})
        output = respuesta["output"]
        
        # 6. Intentar parsear JSON
        resultados = parsear_resultado(output)
        
        if resultados is not None:
            return resultados
        
        # Si falla, usar Tavily como respaldo
        resultados_raw = tavily_tool.invoke({"query": tema})
        return [{
            "titulo": res.get("title", "Sin título"),
            "contenido": res.get("content", "")[:500] + "...",
            "enlace": res.get("url", "#")
        } for res in resultados_raw]
        
    except Exception as e:
        print(f"Error crítico: {e}")
        return []