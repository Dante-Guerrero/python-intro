# Nombre: 01-leer-txt.py
# Tema: Lectura de archivos de texto
# Objetivo: Abrir un archivo .txt y mostrar su contenido.
# Como ejecutarlo: python 04-archivos/01-leer-txt.py

from pathlib import Path

# Construimos la ruta del archivo a partir de la ubicacion del script.
ruta_archivo = Path(__file__).parent / "data" / "edicto.txt"

#ruta_archivo = "04-archivos/data/edicto.txt"

# open() permite leer el archivo. encoding="utf-8" evita problemas con acentos.
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)
