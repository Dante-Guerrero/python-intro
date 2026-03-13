# Nombre: 01-pdf-simple-estudiantes.py
# Tema: PDF basico con un loop
# Objetivo: Crear un PDF sencillo escribiendo una lista de estudiantes con un bucle.
# Como ejecutarlo: python 07-ejemplos_avanzados/01-pdf-simple-estudiantes.py
#
# Libreria necesaria:
#   pip install reportlab
# Si tu sistema usa pip3:
#   pip3 install reportlab

from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

carpeta_base = Path(__file__).parent
ruta_pdf = carpeta_base / "pdfs_entrada" / "01-lista-estudiantes.pdf"

# Esta lista servira para recorrer nombres con un loop.
estudiantes = [
    "Ana Perez",
    "Luis Torres",
    "Maria Lopez",
    "Carlos Vega",
    "Julia Ramos",
]

pdf = canvas.Canvas(str(ruta_pdf), pagesize=LETTER)
ancho, alto = LETTER

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(72, alto - 72, "Bienvenidos al curso de Python")

pdf.setFont("Helvetica", 11)
pdf.drawString(72, alto - 100, "Este ejemplo muestra como escribir varias lineas con un loop.")

# Empezamos una altura inicial y bajamos en cada iteracion.
y = alto - 150
for numero, nombre in enumerate(estudiantes, start=1):
    pdf.drawString(90, y, f"{numero}. {nombre}")
    y -= 24

pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(72, 72, "PDF generado automaticamente con reportlab.")

pdf.save()

print("PDF creado en:", ruta_pdf)
