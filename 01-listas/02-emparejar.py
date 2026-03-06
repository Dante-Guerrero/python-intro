# Nombre: 02-emparejar.py
# Tema: Recorrer listas al mismo tiempo
# Objetivo: Usar zip() para unir informacion relacionada.
# Como ejecutarlo: python 01-listas/02-emparejar.py

# Cada lista tiene informacion de la misma posicion.
codigos = ["EXP-001", "EXP-002", "EXP-003"]
estados = ["En revision", "Archivado", "Resuelto"]
prioridades = [1, 2, 1]

# zip() permite recorrer las tres listas en paralelo.
for codigo, estado, prioridad in zip(codigos, estados, prioridades):
    print(codigo, "-", estado, "- prioridad", prioridad)
