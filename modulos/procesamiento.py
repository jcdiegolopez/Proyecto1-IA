# modulos/procesamiento.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_TOKEN"))

def generar_resumen(resultados):
    texto_completo = "\n\n".join([r["contenido"] for r in resultados])

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente que resume información de forma clara y concisa."},
            {"role": "user", "content": f"Resume este texto en 3 párrafos:\n\n{texto_completo}"}
        ]
    )

    return respuesta.choices[0].message.content
