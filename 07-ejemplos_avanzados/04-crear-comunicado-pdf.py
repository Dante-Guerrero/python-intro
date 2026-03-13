# Nombre: 04-crear-comunicado-pdf.py
# Tema: Creacion de un PDF con logo e imagen institucional
# Objetivo: Generar un comunicado de bienvenida al curso y guardarlo en pdfs_entrada.
# Como ejecutarlo: python 07-ejemplos_avanzados/04-crear-comunicado-pdf.py
#
# Libreria necesaria:
#   pip install reportlab
# Si tu sistema usa pip3:
#   pip3 install reportlab
#
# Uso:
# 1. Verifica que el logo exista en 07-ejemplos_avanzados/images/
# 2. Ejecuta este script.
# 3. Se creara un PDF en pdfs_entrada para usarlo luego con el script de unir PDFs.

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas

carpeta_base = Path(__file__).parent
ruta_logo = carpeta_base / "images" / "logo_legaltech.png"
ruta_pdf = carpeta_base / "pdfs_entrada" / "00-comunicado-bienvenida.pdf"

pdf = canvas.Canvas(str(ruta_pdf), pagesize=LETTER)
ancho_pagina, alto_pagina = LETTER
margen = 54

# Definimos algunos colores para que el documento tenga una identidad visual sobria.
color_fondo = colors.HexColor("#F3F4F6")
color_principal = colors.HexColor("#0E3A5D")
color_secundario = colors.HexColor("#C97B39")
color_texto = colors.HexColor("#1E1E1E")
color_panel = colors.white

# Pintamos el fondo completo de la hoja.
pdf.setFillColor(color_fondo)
pdf.rect(0, 0, ancho_pagina, alto_pagina, stroke=0, fill=1)

# Creamos una cabecera blanca para que el logo respire y se vea con nitidez.
pdf.setFillColor(colors.white)
pdf.rect(0, alto_pagina - 135, ancho_pagina, 135, stroke=0, fill=1)

# Agregamos una linea sobria para separar la cabecera del contenido.
pdf.setStrokeColor(colors.HexColor("#D6D9DE"))
pdf.setLineWidth(1)
pdf.line(margen, alto_pagina - 135, ancho_pagina - margen, alto_pagina - 135)

# Dibujamos una tarjeta central blanca para contener el mensaje.
alto_panel = alto_pagina - 190
pdf.setFillColor(color_panel)
pdf.roundRect(margen, 60, ancho_pagina - (margen * 2), alto_panel, 18, stroke=0, fill=1)

# Agregamos un acento lateral para que la composicion no sea plana.
pdf.setFillColor(color_secundario)
pdf.roundRect(margen + 20, alto_pagina - 280, 14, 120, 7, stroke=0, fill=1)

# Dibujamos el logo manteniendo su proporcion original.
logo = ImageReader(str(ruta_logo))
logo_ancho, logo_alto = logo.getSize()
logo_destino_ancho = 180
logo_destino_alto = logo_destino_ancho * (logo_alto / logo_ancho)
pdf.drawImage(
    logo,
    margen,
    alto_pagina - 112,
    width=logo_destino_ancho,
    height=logo_destino_alto,
    mask="auto",
)

# Texto superior corto para contextualizar el documento.
pdf.setFillColor(color_principal)
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(margen + 205, alto_pagina - 52, "CURSO INTRODUCTORIO")
pdf.setFont("Helvetica", 10)
pdf.drawString(margen + 205, alto_pagina - 69, "Primeros pasos en programacion con Python")

# Titulo principal.
pdf.setFillColor(color_principal)
pdf.setFont("Helvetica-Bold", 24)
pdf.drawString(margen + 42, alto_pagina - 180, "Bienvenidos al mundo de Python")

# Subtitulo con tono institucional.
pdf.setFillColor(color_secundario)
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(margen + 42, alto_pagina - 205, "Comunicado de apertura del curso")

styles = getSampleStyleSheet()
estilo_cuerpo = ParagraphStyle(
    "Cuerpo",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=11,
    leading=18,
    textColor=color_texto,
)
estilo_cita = ParagraphStyle(
    "Cita",
    parent=styles["BodyText"],
    fontName="Helvetica-BoldOblique",
    fontSize=12,
    leading=18,
    textColor=color_principal,
)

parrafos = [
    "Queridos estudiantes:",
    (
        "Hoy empieza una etapa nueva. Python no es solo un lenguaje de programacion: "
        "es una forma de aprender a pensar con claridad, resolver problemas reales y "
        "descubrir que una idea bien ordenada puede convertirse en una herramienta util."
    ),
    (
        "Cada ejercicio que desarrollen sera una pequena victoria. No importa si al "
        "principio algo parece dificil. Aprender a programar tambien es aprender a "
        "tener paciencia, a observar con detalle y a confiar en el proceso."
    ),
    (
        "Deseamos que este curso les recuerde que el conocimiento tecnico puede estar "
        "al servicio de la creatividad, de la profesion y de los proyectos que todavia "
        "no imaginan."
    ),
]

# Dibujamos una cita destacada con una linea decorativa.
pdf.setStrokeColor(color_secundario)
pdf.setLineWidth(2)
pdf.line(margen + 42, alto_pagina - 235, margen + 142, alto_pagina - 235)

cita = Paragraph(
    "Cada linea de codigo es una invitacion a pensar, crear y avanzar con confianza.",
    estilo_cita,
)
cita_ancho, cita_alto = cita.wrap(ancho_pagina - 180, 60)
cita.drawOn(pdf, margen + 42, alto_pagina - 290)

# Dibujamos el cuerpo del comunicado con ajuste automatico de linea.
y = alto_pagina - 365
for texto in parrafos:
    parrafo = Paragraph(texto, estilo_cuerpo)
    ancho_parrafo = ancho_pagina - (margen * 2) - 84
    parrafo_ancho, parrafo_alto = parrafo.wrap(ancho_parrafo, 200)
    parrafo.drawOn(pdf, margen + 42, y - parrafo_alto)
    y -= parrafo_alto + 18

# Cierre y firma.
pdf.setFillColor(color_principal)
pdf.setFont("Helvetica-Bold", 11)
pdf.drawString(margen + 42, 125, "Sean bienvenidos.")
pdf.setFillColor(color_texto)
pdf.setFont("Helvetica", 11)
pdf.drawString(margen + 42, 105, "Este es el inicio de un camino que vale la pena recorrer.")

pdf.setFillColor(color_principal)
pdf.setFont("Helvetica-Bold", 11)
pdf.drawString(margen + 42, 78, "Equipo docente del curso")

# Pie de pagina con una pequena marca visual.
pdf.setStrokeColor(color_principal)
pdf.setLineWidth(1)
pdf.line(margen, 48, ancho_pagina - margen, 48)
pdf.setFillColor(color_principal)
pdf.setFont("Helvetica", 9)
pie = "Comunicado generado automaticamente para el ejercicio de union de PDFs"
pie_x = (ancho_pagina - stringWidth(pie, "Helvetica", 9)) / 2
pdf.drawString(pie_x, 34, pie)

pdf.save()

print("Comunicado creado en:", ruta_pdf)
