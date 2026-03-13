# Nombre: 08-pyautogui-basico.py
# Tema: Automatizacion basica con pyautogui
# Objetivo: Mostrar acciones simples de mouse, teclado y captura de pantalla.
# Como ejecutarlo: python 07-ejemplos_avanzados/08-pyautogui-basico.py
#
# Libreria necesaria:
#   pip install pyautogui
# Si tu sistema usa pip3:
#   pip3 install pyautogui
#
# Nota importante:
# pyautogui controla tu mouse y tu teclado de verdad.
# Mueve el cursor a una esquina de la pantalla para activar el mecanismo
# de seguridad de pyautogui y detener el script si algo sale mal.
# Este ejemplo deja activa la opcion de Windows y una opcion comentada
# para macOS. Si usas Mac, comenta la linea de Windows y descomenta
# la linea de TextEdit.

from pathlib import Path
import subprocess
import time

import pyautogui

# Esta opcion hace que el mouse pueda cancelar la ejecucion
# cuando se mueve a la esquina superior izquierda.
pyautogui.FAILSAFE = True

# Agregamos una pausa pequena entre acciones para que se vean mejor.
pyautogui.PAUSE = 1

print("Tamano de pantalla:", pyautogui.size())
print("Posicion actual del mouse:", pyautogui.position())
print("El script empezara en 3 segundos...")
time.sleep(3)

# Abrimos el Bloc de notas usando el programa notepad.exe de Windows.
subprocess.Popen(["notepad.exe"])

# Opcion para macOS:
# Abre TextEdit. Si usas Mac, comenta la linea de arriba y descomenta esta.
# subprocess.Popen(["open", "-a", "TextEdit"])

# Esperamos un momento para que la ventana se abra y quede activa.
time.sleep(2)

# Escribimos un texto en la ventana del Bloc de notas.
pyautogui.write("Hola, este texto fue escrito con pyautogui.", interval=0.05)
pyautogui.press("enter")
pyautogui.write("Este ejemplo abrio el Bloc de notas automaticamente.", interval=0.05)
pyautogui.press("enter")
pyautogui.write("Tambien puede tomar una captura de pantalla al final.", interval=0.05)

# Guardamos una captura de pantalla en la carpeta actual.
ruta_captura = Path(__file__).parent / "captura_pyautogui.png"
pyautogui.screenshot(str(ruta_captura))

print("Captura guardada en:", ruta_captura)
print("Ejemplo terminado.")
