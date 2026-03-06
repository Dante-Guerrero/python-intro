# Nombre: 03-plazo-simple.py
# Tema: Calculo simple de plazos
# Objetivo: Sumar dias a una fecha para obtener un vencimiento.
# Como ejecutarlo: python 03-fechas/03-plazo-simple.py

from datetime import datetime, timedelta

# Imaginemos que un documento fue notificado en esta fecha.
fecha_notificacion = datetime.strptime("2026-03-06", "%Y-%m-%d")

# timedelta(days=5) representa un plazo de 5 dias.
plazo = timedelta(days=5)
fecha_vencimiento = fecha_notificacion + plazo

print("Fecha de notificacion:", fecha_notificacion.date())
print("Plazo en dias:", plazo.days)
print("Fecha de vencimiento:", fecha_vencimiento.date())
