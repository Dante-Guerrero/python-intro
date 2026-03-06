# Nombre: 03-contar-por-estado.py
# Tema: Conteo por categorias con pandas
# Objetivo: Contar cuantos registros hay en cada estado.
# Como ejecutarlo: python 05-datos/03-contar-por-estado.py

import pandas as pd
from pathlib import Path

# Leemos el archivo con los datos.
ruta_csv = Path(__file__).parent / "data" / "multas.csv"
tabla = pd.read_csv(ruta_csv)

# value_counts() cuenta cuantas veces aparece cada valor.
conteo_estados = tabla["estado"].value_counts()
print(conteo_estados)
