# Nombre: 04-promedio-multas.py
# Tema: Promedios con pandas
# Objetivo: Calcular el promedio de una columna numerica.
# Como ejecutarlo: python 05-datos/04-promedio-multas.py

import pandas as pd
from pathlib import Path

# Abrimos el archivo CSV con los montos.
ruta_csv = Path(__file__).parent / "data" / "multas.csv"
tabla = pd.read_csv(ruta_csv)

# mean() calcula el promedio de la columna monto.
promedio_monto = tabla["monto"].mean()
print("Promedio de multas:", promedio_monto)
