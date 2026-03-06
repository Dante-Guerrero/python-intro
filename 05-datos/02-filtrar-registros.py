# Nombre: 02-filtrar-registros.py
# Tema: Filtrar registros con pandas
# Objetivo: Mostrar solo los expedientes que siguen en revision.
# Como ejecutarlo: python 05-datos/02-filtrar-registros.py

import pandas as pd
from pathlib import Path

# Leemos el archivo CSV con pandas.
ruta_csv = Path(__file__).parent / "data" / "multas.csv"
tabla = pd.read_csv(ruta_csv)

# Filtramos solo las filas donde el estado sea "Pendiente".
pendientes = tabla[tabla["estado"] == "Pendiente"]
print(pendientes)
