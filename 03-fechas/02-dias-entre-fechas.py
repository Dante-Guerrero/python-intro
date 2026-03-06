# Nombre: 02-dias-entre-fechas.py
# Tema: Diferencia entre fechas
# Objetivo: Calcular cuantos dias hay entre dos fechas.
# Como ejecutarlo: python 03-fechas/02-dias-entre-fechas.py

from datetime import datetime

# strptime() convierte un texto en una fecha real.
fecha_presentacion = datetime.strptime("2026-03-01", "%Y-%m-%d")
fecha_audiencia = datetime.strptime("2026-03-18", "%Y-%m-%d")

# Al restar dos fechas obtenemos una diferencia de tiempo.
diferencia = fecha_audiencia - fecha_presentacion

print("Fecha de presentacion:", fecha_presentacion.date())
print("Fecha de audiencia:", fecha_audiencia.date())
print("Dias entre ambas fechas:", diferencia.days)
