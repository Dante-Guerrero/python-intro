# Nombre: 03-crear-cartas-pdf.py
# Tema: Creacion de cartas PDF desde CSV
# Objetivo: Generar una carta PDF por cada registro de un archivo CSV.
# Como ejecutarlo: python 07-ejemplos_avanzados/03-crear-cartas-pdf.py
#
# Libreria necesaria:
#   pip install reportlab
# Si tu sistema usa pip3:
#   pip3 install reportlab
#
# El archivo de entrada debe tener columnas como:
# nombre,domicilio,distrito,motivo
#
# Este ejemplo guarda las cartas dentro de pdfs_entrada para que luego
# puedan servir como insumo directo del script de unir PDFs.

import csv
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

carpeta_base = Path(__file__).parent
ruta_csv = carpeta_base / "data" / "cartas_destinatarios.csv"
carpeta_salida = carpeta_base / "pdfs_entrada"
carpeta_salida.mkdir(parents=True, exist_ok=True)


def limpiar_nombre_archivo(texto):
    # Reemplazamos espacios por guiones bajos para crear nombres validos.
    return texto.lower().replace(" ", "_")


with open(ruta_csv, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for numero, fila in enumerate(lector, start=3):
        nombre_archivo = f"{numero:02d}-carta-{limpiar_nombre_archivo(fila['nombre'])}.pdf"
        ruta_pdf = carpeta_salida / nombre_archivo

        # canvas.Canvas permite escribir texto y formas sobre un PDF nuevo.
        pdf = canvas.Canvas(str(ruta_pdf), pagesize=LETTER)
        ancho, alto = LETTER

        # Escribimos una carta simple, linea por linea.
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(72, alto - 72, "Carta de notificacion")

        pdf.setFont("Helvetica", 11)
        pdf.drawString(72, alto - 120, f"Nombre: {fila['nombre']}")
        pdf.drawString(72, alto - 145, f"Domicilio: {fila['domicilio']}")
        pdf.drawString(72, alto - 170, f"Distrito: {fila['distrito']}")

        pdf.drawString(72, alto - 220, "Estimado/a:")
        pdf.drawString(
            72,
            alto - 245,
            f"Por medio de la presente se le informa lo siguiente: {fila['motivo']}",
        )
        pdf.drawString(
            72,
            alto - 295,
            "Este documento fue generado automaticamente a partir de un archivo CSV.",
        )
        pdf.drawString(72, alto - 345, "Atentamente,")
        pdf.drawString(72, alto - 370, "Oficina de Tramite Documentario")

        # Guardamos el archivo PDF en disco.
        pdf.save()
        print("Carta creada:", ruta_pdf)
