''' Mi primer proyecto para el portfolio
    Consiste hacer un programa que traduzca a voz un archivo o pagina web '''

import nltk
from newspaper import Article
from gtts import gTTS
import os
import platform
import subprocess

# Descargar recursos necesarios para nltk
nltk.download('punkt')

def reproducir_mp3(ruta_archivo):
    
    # Utilizar el comando afplay para reproducir el archivo MP3 des de MacOs
    # subprocess.run(["afplay", ruta_archivo]) 

    
    # Utilizar el comando ffplay para reproducir el archivo MP3 des de Linux
    #subprocess.run(["ffplay", ruta_archivo]) 
    
    subprocess.run(["ffplay", "-nodisp", "-autoexit", ruta_archivo])
    # ruta_mp3 = "/root/salida.mp3"  # Ajusta el nombre del archivo según sea necesario 
    # reproducir_mp3(ruta_mp3) 


def convertir_articulo_a_audio(url):
    # Obtener el contenido del artículo
    article = Article(url)
    article.download()
    article.parse()

    # Obtener el texto del artículo
    texto_articulo = article.text

    # Crear un objeto gTTS (Google Text-to-Speech) con el texto del artículo
    tts = gTTS(text=texto_articulo, lang='es')  # Puedes ajustar el idioma según tus necesidades

    # Guardar el archivo de audio en formato MP3
    tts.save("salida.mp3")

    # Reproducir el archivo de audio (puedes utilizar un reproductor de audio externo)
    reproducir_mp3("salida.mp3")

if __name__ == "__main__":
    # Proporciona la URL del artículo que deseas convertir
    url_articulo = input("Introduce la URL del artículo: ")
    convertir_articulo_a_audio(url_articulo)
