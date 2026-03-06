# Nombre: 03-leer-csv.py
# Tema: Lectura basica de CSV
# Objetivo: Leer un archivo CSV simple usando la libreria csv.
# Como ejecutarlo: python 04-archivos/03-leer-csv.py

import csv
from pathlib import Path

# Ubicamos el archivo de datos.
ruta_csv = Path(__file__).parent / "data" / "expedientes.csv"

# csv.DictReader() lee cada fila como un diccionario.
with open(ruta_csv, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        print(
            fila["codigo"],
            "-",
            fila["estado"],
            "- responsable:",
            fila["responsable"],
        )
