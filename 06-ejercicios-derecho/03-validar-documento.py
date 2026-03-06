# Nombre: 03-validar-documento.py
# Tema: Validacion de formato de texto
# Objetivo: Revisar si un codigo sigue un formato simple.
# Como ejecutarlo: python 06-ejercicios-derecho/03-validar-documento.py

# Queremos comprobar si el codigo empieza con DOC-.
codigo_documento = "DOC-2026-15"

if codigo_documento.startswith("DOC-"):
    print("Formato valido")
else:
    print("Formato invalido")
