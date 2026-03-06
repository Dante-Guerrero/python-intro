# Nombre: 03-convertirtipos.py
# Tema: Conversion de tipos
# Objetivo: Entender que input() devuelve texto y aprender a convertirlo.
# Como ejecutarlo: python 00-basicos/03-convertirtipos.py

# Aunque el usuario escriba un numero, input() lo guarda como texto.
texto_numero = input("Escribe un numero: ")
print("Tipo inicial:", type(texto_numero))

# int() convierte el texto en numero entero.
numero_entero = int(texto_numero)
print("Tipo despues de int():", type(numero_entero))

# str() vuelve a convertir el numero en texto.
numero_como_texto = str(numero_entero)
print("Tipo despues de str():", type(numero_como_texto))
