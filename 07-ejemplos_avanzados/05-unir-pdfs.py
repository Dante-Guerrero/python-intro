# Nombre: 05-unir-pdfs.py
# Tema: Union de PDF con pypdf
# Objetivo: Recorrer una carpeta con varios PDF y combinarlos en un solo archivo.
# Como ejecutarlo: python 07-ejemplos_avanzados/05-unir-pdfs.py
#
# Libreria necesaria:
#   pip install pypdf
# Si tu sistema usa pip3:
#   pip3 install pypdf
#
# Uso:
# 1. Coloca tus PDF dentro de 07-ejemplos_avanzados/pdfs_entrada/
# 2. Ejecuta este script.
# 3. El archivo combinado se guardara en pdfs_salida/documento_unido.pdf

from pathlib import Path

from pypdf import PdfWriter

carpeta_base = Path(__file__).parent
carpeta_entrada = carpeta_base / "pdfs_entrada"
carpeta_salida = carpeta_base / "pdfs_salida"
archivo_salida = carpeta_salida / "documento_unido.pdf"

# Creamos la carpeta de salida si todavia no existe.
carpeta_salida.mkdir(exist_ok=True)

# Buscamos todos los archivos .pdf y los ordenamos por nombre.
archivos_pdf = sorted(carpeta_entrada.glob("*.pdf"))

if not archivos_pdf:
    print("No se encontraron PDF en:", carpeta_entrada)
    print("Agrega archivos .pdf a esa carpeta y vuelve a ejecutar el script.")
else:
    writer = PdfWriter()

    # Agregamos cada PDF al documento final.
    # En versiones recientes de pypdf, PdfWriter.append() reemplaza
    # el uso tradicional de PdfMerger.
    for ruta_pdf in archivos_pdf:
        print("Agregando:", ruta_pdf.name)
        writer.append(str(ruta_pdf))

    # Guardamos el resultado combinado.
    with open(archivo_salida, "wb") as archivo_final:
        writer.write(archivo_final)

    writer.close()

    print("PDF combinado creado en:", archivo_salida)
