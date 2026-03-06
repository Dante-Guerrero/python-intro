# Nombre: 01-fecha-actual.py
# Tema: Fecha actual
# Objetivo: Obtener la fecha de hoy con datetime.
# Como ejecutarlo: python 03-fechas/01-fecha-actual.py

from datetime import date

# date.today() devuelve la fecha actual del sistema.
hoy = date.today()

print("Fecha de hoy:", hoy)
print("Anio:", hoy.year)
print("Mes:", hoy.month)
print("Dia:", hoy.day)
