import streamlit as st
from modulos.busqueda import buscar_informacion
from modulos.procesamiento import generar_resumen
from modulos.visualizacion import generar_nube_palabras
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Streamlit
st.title("🔍 Asistente de Investigación Digital")
tema = st.text_input("Ingresa un tema de investigación:")

if tema:
    st.info(f"Buscando: {tema}...")
    
    # 1. Búsqueda con Tavily
    resultados = buscar_informacion(tema)
    st.subheader("📄 Resultados Encontrados")
    for resultado in resultados:
        st.write(f"**{resultado['titulo']}**")
        st.write(resultado['contenido'])
        st.write(f"[Leer más]({resultado['enlace']})")
    
    # 2. Resumen con OpenAI
    st.subheader("✍️ Resumen Automático")
    resumen = generar_resumen(resultados)
    st.write(resumen)
    
    # 3. Nube de palabras
    st.subheader("☁️ Nube de Palabras Clave")
    figura = generar_nube_palabras(resultados)
    st.pyplot(figura)
