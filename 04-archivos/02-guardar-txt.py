# Nombre: 02-guardar-txt.py
# Tema: Escritura de archivos de texto
# Objetivo: Guardar un mensaje en un archivo .txt nuevo.
# Como ejecutarlo: python 04-archivos/02-guardar-txt.py

from pathlib import Path

# Definimos donde se guardara el archivo.
ruta_salida = Path(__file__).parent / "data" / "nota_generada.txt"
texto = "Se registro una observacion simple sobre el expediente EXP-010."

# El modo "w" crea el archivo o reemplaza su contenido si ya existe.
with open(ruta_salida, "w", encoding="utf-8") as archivo:
    archivo.write(texto)

print("Archivo guardado en:", ruta_salida)
