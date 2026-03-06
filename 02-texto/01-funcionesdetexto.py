# Nombre: 01-funcionesdetexto.py
# Tema: Funciones y metodos de texto
# Objetivo: Practicar operaciones simples para limpiar y revisar textos.
# Como ejecutarlo: python 02-texto/01-funcionesdetexto.py

# Usamos un texto con espacios al inicio y al final para notar el cambio.
texto = "   Hola, Mundo Python   "
print("Texto original:", repr(texto))

# strip() elimina espacios sobrantes al inicio y al final.
texto_sin_espacios = texto.strip()
print("Despues de strip():", repr(texto_sin_espacios))

# lower() y upper() ayudan a normalizar mayusculas y minusculas.
print("En minusculas:", texto_sin_espacios.lower())
print("En mayusculas:", texto_sin_espacios.upper())

# split() separa un texto en partes.
frase = "python es simple"
palabras = frase.split()
print("Palabras separadas:", palabras)

# Tambien podemos separar usando un caracter especifico.
linea_csv = "Ana,Bruno,Carla"
nombres = linea_csv.split(",")
print("Nombres desde CSV:", nombres)

# replace() cambia una parte del texto por otra.
mensaje = "Me gusta Java"
print("Texto reemplazado:", mensaje.replace("Java", "Python"))

# startswith() y endswith() verifican inicio y final del texto.
archivo = "reporte_2026.pdf"
print("Empieza con 'reporte_'?:", archivo.startswith("reporte_"))
print("Termina en '.pdf'?:", archivo.endswith(".pdf"))

# Este ejemplo muestra una limpieza tipica antes de validar un correo.
correo = "  estudiante@ejemplo.com  "
correo_limpio = correo.strip().lower()
print("Correo limpio:", correo_limpio)
