# modulos/visualizacion.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generar_nube_palabras(resultados):
    texto = " ".join([r["contenido"] for r in resultados])
    nube = WordCloud(width=800, height=400, background_color='white').generate(texto)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(nube, interpolation='bilinear')
    ax.axis('off')

    return fig
