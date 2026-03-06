# Nombre: 08-buclewhile.py
# Tema: Repeticiones con while
# Objetivo: Repetir una accion hasta que se cumpla una condicion.
# Como ejecutarlo: python 00-basicos/08-buclewhile.py

# Empezamos con una variable vacia.
clave_ingresada = ""

# El ciclo continua mientras la clave sea incorrecta.
while clave_ingresada != "1234":
    clave_ingresada = input("Escribe la clave de acceso: ")

print("Acceso permitido")
