# Nombre: 02-pdf-logo-centrado.py
# Tema: PDF con imagen centrada
# Objetivo: Crear un PDF simple colocando el logo del curso en el centro de la pagina.
# Como ejecutarlo: python 07-ejemplos_avanzados/02-pdf-logo-centrado.py
#
# Libreria necesaria:
#   pip install reportlab
# Si tu sistema usa pip3:
#   pip3 install reportlab

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

carpeta_base = Path(__file__).parent
ruta_logo = carpeta_base / "images" / "logo_legaltech.png"
ruta_pdf = carpeta_base / "pdfs_entrada" / "02-logo-centrado.pdf"

pdf = canvas.Canvas(str(ruta_pdf), pagesize=LETTER)
ancho, alto = LETTER

# Usamos un fondo claro para que el logo se vea limpio.
pdf.setFillColor(colors.HexColor("#F7F7F7"))
pdf.rect(0, 0, ancho, alto, stroke=0, fill=1)

pdf.setFillColor(colors.HexColor("#0E3A5D"))
pdf.setFont("Helvetica-Bold", 18)
pdf.drawCentredString(ancho / 2, alto - 80, "Logo del curso centrado en el PDF")

logo = ImageReader(str(ruta_logo))
logo_ancho, logo_alto = logo.getSize()
logo_destino_ancho = 240
logo_destino_alto = logo_destino_ancho * (logo_alto / logo_ancho)
posicion_x = (ancho - logo_destino_ancho) / 2
posicion_y = (alto - logo_destino_alto) / 2 - 20

# drawImage permite colocar una imagen en una posicion exacta.
pdf.drawImage(
    logo,
    posicion_x,
    posicion_y,
    width=logo_destino_ancho,
    height=logo_destino_alto,
    mask="auto",
)

pdf.setFont("Helvetica", 11)
pdf.setFillColor(colors.HexColor("#444444"))
pdf.drawCentredString(
    ancho / 2,
    90,
    "Este ejemplo agrega una imagen institucional en el centro de la pagina.",
)

pdf.save()

print("PDF creado en:", ruta_pdf)
