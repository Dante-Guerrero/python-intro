# demo_strings.py
# Un mini “laboratorio” de strings: métodos útiles y lo que hacen.
# Porque sí, la gente escribe con espacios, mayúsculas raras y separadores creativos.

texto = "   Hola, Mundo Python   "

print("Texto original:", repr(texto))
# repr() muestra el string “tal cual”, incluyendo espacios y caracteres invisibles.

# 1) .strip()  -> quita espacios (y saltos de línea) al inicio y al final
sin_bordes = texto.strip()
print("\n1) .strip()")
print("Resultado:", repr(sin_bordes))

# 2) .lower() / .upper() -> normaliza mayúsculas/minúsculas
print("\n2) .lower() / .upper()")
print("lower():", sin_bordes.lower())
print("upper():", sin_bordes.upper())

# 3) .split() -> separa un string en partes (lista)
# - si no le pasas nada, separa por espacios (uno o varios)
# - si le pasas un separador, usa ese separador
print("\n3) .split()")
frase = "python  es   simple"
print("Frase:", repr(frase))
print("split() por espacios:", frase.split())

csv = "Ana,Bruno,Carla"
print("CSV:", repr(csv))
print("split(','):", csv.split(","))

# 4) .replace() -> reemplaza una parte por otra
print("\n4) .replace()")
mensaje = "Me gusta Java"
print("Original:", mensaje)
print("replace('Java','Python'):", mensaje.replace("Java", "Python"))

# 5) .startswith() / .endswith() -> verifica prefijo o sufijo (devuelve True/False)
print("\n5) .startswith() / .endswith()")
archivo = "reporte_2026.pdf"
print("Archivo:", archivo)
print("startswith('reporte_'):", archivo.startswith("reporte_"))
print("endswith('.pdf'):", archivo.endswith(".pdf"))

# Bonus: ejemplo típico de “limpieza” real
print("\nBONUS: limpieza típica antes de validar")
correo = "  Dante@Ejemplo.COM  "
correo_limpio = correo.strip().lower()
print("Correo original:", repr(correo))
print("Correo limpio:", repr(correo_limpio))
print("¿Termina en .com?:", correo_limpio.endswith(".com"))