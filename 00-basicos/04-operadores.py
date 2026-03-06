# Nombre: 04-operadores.py
# Tema: Operadores aritmeticos y comparaciones
# Objetivo: Practicar operaciones basicas con dos numeros.
# Como ejecutarlo: python 00-basicos/04-operadores.py

# Pedimos dos numeros enteros al usuario.
primer_numero = int(input("Escribe el primer numero: "))
segundo_numero = int(input("Escribe el segundo numero: "))

# Mostramos operaciones aritmeticas basicas.
print("Suma:", primer_numero + segundo_numero)
print("Resta:", primer_numero - segundo_numero)
print("Multiplicacion:", primer_numero * segundo_numero)

# Solo dividimos si el segundo numero no es cero.
if segundo_numero != 0:
    print("Division:", primer_numero / segundo_numero)
    print("Division entera:", primer_numero // segundo_numero)
    print("Residuo:", primer_numero % segundo_numero)
    print("Es multiplo?:", primer_numero % segundo_numero == 0)
else:
    print("Division: no se puede dividir entre cero")
    print("Division entera: no se puede dividir entre cero")
    print("Residuo: no se puede dividir entre cero")
    print("Es multiplo?: no aplica cuando el segundo numero es cero")

# Tambien podemos comparar valores.
print("Potencia:", primer_numero ** segundo_numero)
print("El primer numero es mayor?:", primer_numero > segundo_numero)
