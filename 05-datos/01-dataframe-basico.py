# Nombre: 01-dataframe-basico.py
# Tema: Primer DataFrame con pandas
# Objetivo: Crear una tabla simple en memoria y verla en pantalla.
# Como ejecutarlo: python 05-datos/01-dataframe-basico.py

import pandas as pd

# Creamos un diccionario con columnas sencillas.
datos = {
    "expediente": ["EXP-001", "EXP-002", "EXP-003"],
    "estado": ["En revision", "Archivado", "En revision"],
    "monto": [1500, 0, 800],
}

# pd.DataFrame() convierte el diccionario en una tabla.
tabla = pd.DataFrame(datos)
print(tabla)
#print(tabla.iloc[[0]])
