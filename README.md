# 🧠 Asistente de Investigación Digital

Este es un proyecto en Python con Streamlit que utiliza herramientas de Inteligencia Artificial para **buscar, procesar y visualizar información** de forma automática.

## 🚀 ¿Qué hace este asistente?

1. **Búsqueda Inteligente:** Consulta internet usando la API de Tavily a través de un agente ReAct de LangChain.
2. **Resumen Automático:** Genera un resumen claro y conciso con la ayuda de un modelo GPT de OpenAI.
3. **Visualización:** Crea una nube de palabras clave basada en los resultados obtenidos.

---

## 📁 Estructura del Proyecto

```
proyecto/
├── app.py
├── modulos/
│   ├── busqueda.py
│   ├── procesamiento.py
│   └── visualizacion.py
├── .env
└── README.md
```

### `app.py`
Archivo principal. Corre la aplicación en Streamlit y orquesta el flujo de búsqueda, resumen y visualización.

### `modulos/busqueda.py`
Contiene la función `buscar_informacion(tema)` que usa un agente ReAct con Tavily para buscar en internet y retornar los resultados en formato Markdown.

### `modulos/procesamiento.py`
Contiene `generar_resumen(resultados)`, que concatena los resultados y solicita un resumen al modelo GPT.

### `modulos/visualizacion.py`
Incluye `generar_nube_palabras(resultados)` que genera una nube de palabras clave usando `wordcloud` y `matplotlib`.

---

## ⚙️ Instrucciones de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/asistente-investigacion.git
cd asistente-investigacion
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear el archivo `.env`

Incluir las claves de API:

```env
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
```

### 4. Correr la app

```bash
streamlit run app.py
```

---

## 🤔 ¿Por qué usar IA para investigar?

El uso de inteligencia artificial para la búsqueda y procesamiento de información **acelera el acceso al conocimiento** y ayuda a **sintetizar grandes volúmenes de datos**. Sin embargo, también conlleva riesgos:

- La IA puede **hallar resultados sesgados o inexactos** si no se supervisa correctamente.
- Los resúmenes automáticos **pueden omitir matices importantes** del texto original.
- Es vital que el humano mantenga el **criterio y pensamiento crítico** al usar estos resultados, para no delegar completamente la interpretación del contenido.


---

## 🫂 Integrantes

- Diego López **23242**
- Nicole Rivera **23451**
