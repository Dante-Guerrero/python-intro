# Nombre: 06-grafico-barras-csv.py
# Tema: Graficos con matplotlib
# Objetivo: Leer un CSV y construir un grafico de barras sencillo.
# Como ejecutarlo: python 07-ejemplos_avanzados/06-grafico-barras-csv.py
#
# Libreria necesaria:
#   pip install matplotlib
# Si tu sistema usa pip3:
#   pip3 install matplotlib

import csv
from pathlib import Path

import matplotlib.pyplot as plt

ruta_csv = Path(__file__).parent / "data" / "grafico_ventas.csv"
ruta_imagen = Path(__file__).parent / "grafico_ventas.png"

categorias = []
valores = []

# Leemos el CSV con csv.DictReader para obtener cada fila como diccionario.
with open(ruta_csv, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        categorias.append(fila["categoria"])
        valores.append(int(fila["total"]))

# Creamos la figura y dibujamos las barras.
plt.figure(figsize=(8, 5))
barras = plt.bar(categorias, valores, color="#2f6db3")
plt.title("Ventas por categoria")
plt.xlabel("Categoria")
plt.ylabel("Total")

# Escribimos el valor encima de cada barra para hacer el grafico mas claro.
for barra, valor in zip(barras, valores):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        valor + 1,
        str(valor),
        ha="center",
    )

plt.tight_layout()

# Guardamos una copia del grafico en PNG y luego lo mostramos en pantalla.
plt.savefig(ruta_imagen)
plt.show()

print("Grafico guardado en:", ruta_imagen)
