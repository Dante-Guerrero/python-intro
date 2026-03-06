# Nombre: 02-revision-expedientes.py
# Tema: Revision de estados
# Objetivo: Recorrer una lista de expedientes y mostrar su situacion.
# Como ejecutarlo: python 06-ejercicios-derecho/02-revision-expedientes.py

# Cada elemento de la lista es un diccionario con datos simples.
expedientes = [
    {"codigo": "EXP-001", "estado": "En revision"},
    {"codigo": "EXP-002", "estado": "Archivado"},
    {"codigo": "EXP-003", "estado": "En revision"},
]

for expediente in expedientes:
    print(expediente["codigo"], "->", expediente["estado"])
