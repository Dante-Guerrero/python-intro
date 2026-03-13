# Nombre: 07-enviar-correos.py
# Tema: Envio de correos con smtplib
# Objetivo: Leer una lista de destinatarios desde un CSV y enviar un correo a cada uno.
# Como ejecutarlo: python 07-ejemplos_avanzados/07-enviar-correos.py
#
# Librerias:
# Este ejemplo usa solo bibliotecas incluidas en Python:
#   smtplib
#   csv
#   email.message
#
# Antes de usarlo:
# 1. Edita las variables REMITENTE, CLAVE y SERVIDOR_SMTP.
# 2. Revisa el puerto correcto de tu proveedor.
# 3. Si usas Gmail u otro servicio moderno, normalmente necesitas una
#    clave de aplicacion en lugar de tu contrasena principal.
#
# El CSV de ejemplo tiene columnas:
# correo,nombre

import csv
import smtplib
from email.message import EmailMessage
from pathlib import Path

# Configuracion del remitente.
# Cambia estos valores por los de tu cuenta antes de enviar correos reales.
REMITENTE = "dguerrerob@cientifica.edu.pe"
CLAVE = "sepgyk-pezDec-xotbo7"
SERVIDOR_SMTP = "smtp.ejemplo.com"
PUERTO_SMTP = 587

ruta_csv = Path(__file__).parent / "data" / "destinatarios.csv"


def crear_mensaje(destinatario, nombre):
    # Construimos un mensaje simple en texto plano.
    mensaje = EmailMessage()
    mensaje["Subject"] = "Comunicado automatico"
    mensaje["From"] = REMITENTE
    mensaje["To"] = destinatario
    mensaje.set_content(
        f"Hola {nombre},\n\n"
        "Este es un correo de ejemplo enviado desde Python.\n"
        "Puedes adaptar este texto a tus necesidades.\n\n"
        "Saludos."
    )
    return mensaje


with open(ruta_csv, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    destinatarios = list(lector)

if REMITENTE == "tu_correo@ejemplo.com":
    print("Debes editar la configuracion del remitente antes de enviar correos.")
else:
    # Nos conectamos al servidor SMTP y activamos el cifrado TLS.
    with smtplib.SMTP(SERVIDOR_SMTP, PUERTO_SMTP) as servidor:
        servidor.starttls()
        servidor.login(REMITENTE, CLAVE)

        for fila in destinatarios:
            mensaje = crear_mensaje(fila["correo"], fila["nombre"])
            servidor.send_message(mensaje)
            print("Correo enviado a:", fila["correo"])
