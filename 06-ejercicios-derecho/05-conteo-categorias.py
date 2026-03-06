# Nombre: 05-conteo-categorias.py
# Tema: Conteo por categoria
# Objetivo: Contar cuantos casos hay en cada tipo de tramite.
# Como ejecutarlo: python 06-ejercicios-derecho/05-conteo-categorias.py

casos = ["Laboral", "Civil", "Civil", "Penal", "Laboral", "Civil"]
conteo = {}

# Recorremos la lista y sumamos una unidad por cada categoria.
for categoria in casos:
    if categoria in conteo:
        conteo[categoria] = conteo[categoria] + 1
    else:
        conteo[categoria] = 1

print(conteo)
