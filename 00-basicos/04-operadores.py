# Ejercicio: Operadores con input y output (con comentarios por operación)

a = int(input("a: "))
b = int(input("b: "))

print(f"a+b = {a + b}")      # Suma
print(f"a-b = {a - b}")      # Resta
print(f"a*b = {a * b}")      # Multiplicación

# División y derivados (solo si b no es 0)
if b != 0:
    print(f"a/b = {a / b}")          # División (resultado decimal)
    print(f"a//b = {a // b}")        # División entera (cociente sin decimales)
    print(f"a%b = {a % b}")          # Módulo (residuo de la división)
    print(f"a es múltiplo de b = {a % b == 0}")  # Verifica si a es múltiplo de b
else:
    print("a/b = No se puede dividir entre 0")   # División (error por 0)
    print("a//b = No se puede dividir entre 0")  # División entera (error por 0)
    print("a%b = No se puede dividir entre 0")   # Módulo (error por 0)
    print("a es múltiplo de b = No aplica (b=0)")# Múltiplo no definido si b=0

print(f"a**b = {a ** b}")    # Potencia (a elevado a b)
print(f"a>b = {a > b}")      # Comparación: ¿a es mayor que b?