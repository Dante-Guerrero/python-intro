# Nombre: 04-buscar-palabra-clave.py
# Tema: Busqueda simple de texto
# Objetivo: Detectar si una palabra aparece dentro de un documento.
# Como ejecutarlo: python 06-ejercicios-derecho/04-buscar-palabra-clave.py

texto_resolucion = "La resolucion declara fundada la solicitud presentada por la parte demandante."
palabra_clave = "fundada"

# Convertimos ambos textos a minusculas para evitar problemas de mayusculas.
if palabra_clave.lower() in texto_resolucion.lower():
    print("La palabra clave si aparece en el texto")
else:
    print("La palabra clave no aparece en el texto")
