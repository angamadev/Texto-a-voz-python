# Mi pequeño proyecto Conversor de Artículo a Voz 🎧

Este proyecto es una herramienta simple pero potente que convierte el texto de un artículo o página web a audio usando Google Text-to-Speech (gTTS). Es ideal para aquellos que desean escuchar artículos mientras realizan otras tareas.

---

## 🛠️ Funcionalidad
1. Descarga el contenido de un artículo desde una URL proporcionada.
2. Convierte el texto del artículo a audio en formato MP3.
3. Reproduce el archivo de audio automáticamente.

---

## 📊 Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:
- Python 3.6 o superior.
- Los siguientes paquetes de Python:
  - `nltk`
  - `newspaper3k`
  - `gTTS`

---

## 🚀 Instalación

1. **Clona este repositorio**:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd <NOMBRE_DE_TU_REPOSITORIO>
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Descarga los recursos de `nltk` necesarios**:
   Abre una terminal de Python y ejecuta:
   ```python
   import nltk
   nltk.download('punkt')
   ```

---

## 🔧 Uso

1. Ejecuta el script:
   ```bash
   python texto_voz.py
   ```

2. Introduce la URL del artículo que deseas convertir cuando se te solicite:
   ```text
   Introduce la URL del artículo: https://ejemplo.com/articulo
   ```

3. El programa:
   - Descargará el texto del artículo.
   - Lo convertirá a audio.
   - Reproducirá el archivo MP3.

---

## 🔄 Compatibilidad

Este proyecto ha sido diseñado para ejecutarse en macOS y Linux. En macOS, utiliza `afplay` para reproducir el audio. Puedes ajustar el comando para otros sistemas operativos:
- **Windows**: Usa un reproductor como `playsound` o `winsound`.
- **Linux**: Usa `ffplay` o `aplay`.

---

## 📄 Dependencias

El proyecto utiliza las siguientes bibliotecas:
- **nltk**: Para analizar y tokenizar texto.
- **newspaper3k**: Para extraer contenido de páginas web.
- **gTTS**: Para convertir texto a voz.

---

## 📝 Notas Técnicas
- Ajusta el idioma de `gTTS` en la línea:
  ```python
  tts = gTTS(text=texto_articulo, lang='es')
  ```
  Puedes usar otros idiomas como `'en'` para inglés.

- Si estás en un entorno sin interfaz gráfica, asegúrate de tener un reproductor de audio basado en terminal.

- Recomiendo crear un entorno virtual e instalar las dependencias

   Ejecuta el script:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

---

## 📚 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo como desees. 

---

## 💡 Próximas Mejoras

1. Agregar soporte para múltiples idiomas detectando automáticamente el idioma del artículo.
2. Implementar una interfaz gráfica simple para facilitar su uso.
3. Optimizar la reproducción de audio en sistemas operativos Windows y Linux.

---

¡Gracias por revisar mi proyecto! Si tienes alguna sugerencia o mejora, no dudes en contactarme.
