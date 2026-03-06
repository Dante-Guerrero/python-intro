# Nombre: 06-condicionales2.py
# Tema: Condicionales con varias opciones
# Objetivo: Tomar decisiones con if, elif y else.
# Como ejecutarlo: python 00-basicos/06-condicionales2.py

# Este ejemplo usa tres posibles resultados para una nota.
nota = int(input("Escribe la nota final: "))

if nota >= 18:
    print("Excelente")
elif nota >= 11:
    print("Aprobado")
else:
    print("Desaprobado")
