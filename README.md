# python-intro

Repositorio introductorio para aprender fundamentos de Python paso a paso, con ejemplos pequenos, legibles y pensados para clase.

## Proposito del repositorio

Este material busca acompanar un primer contacto con Python. La idea no es aprender "todo Python", sino practicar las bases con calma: variables, texto, listas, decisiones, repeticiones, archivos, fechas y un primer vistazo a datos tabulares.

## Publico objetivo

Este repositorio esta pensado para estudiantes de derecho sin experiencia previa en programacion.

Si nunca has usado la terminal o nunca has escrito codigo, este material esta hecho para empezar desde cero.

## Requisitos minimos

Necesitas lo siguiente:

- Python instalado en tu computadora
- Git instalado para clonar el repositorio desde GitHub
- Una terminal o consola
- VS Code es opcional, pero puede ayudar a editar y ejecutar archivos con mayor comodidad

## Clonar el repositorio desde GitHub

1. Abre una terminal.
2. Ve a la carpeta donde quieres guardar el proyecto.
3. Ejecuta este comando:

```bash
git clone https://github.com/TU-USUARIO/python-intro.git
```

4. Entra a la carpeta del repositorio:

```bash
cd python-intro
```

Si la URL real del repositorio es distinta, reemplaza `TU-USUARIO` por el nombre correcto en GitHub.

## Como ejecutar scripts

1. Abre una terminal dentro de la carpeta `python-intro`.
2. Ejecuta un archivo con este formato:

```bash
python ruta/del/script.py
```

Por ejemplo:

```bash
python 00-basicos/00-helloworld.py
```

En algunos sistemas, sobre todo macOS o algunas distribuciones de Linux, puede ser necesario usar `python3` en lugar de `python`:

```bash
python3 00-basicos/00-helloworld.py
```

## Instalacion opcional de pandas

La carpeta `05-datos/` usa `pandas` en ejemplos introductorios. Si quieres ejecutar esos archivos, instala la libreria con:

```bash
pip install pandas
```

Si tu sistema usa `pip3`, puedes probar:

```bash
pip3 install pandas
```

## Instalacion opcional de librerias avanzadas

La carpeta `07-ejemplos_avanzados/` incluye ejemplos que usan librerias externas. Puedes instalarlas todas juntas con:

```bash
pip install pyautogui pypdf matplotlib reportlab
```

Si tu sistema usa `pip3`, prueba:

```bash
pip3 install pyautogui pypdf matplotlib reportlab
```

## Estructura del repositorio

```text
python-intro/
|-- README.md
|-- 00-basicos/
|-- 01-listas/
|-- 02-texto/
|-- 03-fechas/
|-- 04-archivos/
|   |-- data/
|-- 05-datos/
|   |-- data/
|-- 06-ejercicios-derecho/
|-- 07-ejemplos_avanzados/
|   |-- data/
|   |-- pdfs_entrada/
|   |-- pdfs_salida/
```

## Ruta sugerida de aprendizaje

Se recomienda avanzar en este orden:

1. `00-basicos/` para entender sintaxis, variables, entradas, condicionales, repeticiones y funciones.
2. `01-listas/` para aprender a guardar y recorrer varios datos.
3. `02-texto/` para limpiar y revisar cadenas de texto.
4. `03-fechas/` para trabajar con fechas y plazos simples.
5. `04-archivos/` para leer y guardar informacion en archivos.
6. `05-datos/` para una introduccion muy basica a tablas con `pandas`.
7. `06-ejercicios-derecho/` para practicar con ejemplos sencillos cercanos al ambito juridico y administrativo.
8. `07-ejemplos_avanzados/` para automatizacion, graficos, PDF y envio de correos.

## Sugerencia para estudiar

Una forma simple de avanzar es esta:

1. Ejecuta un script.
2. Lee los comentarios dentro del archivo.
3. Cambia uno o dos valores.
4. Ejecuta otra vez y observa que cambia.
5. Haz pequenas preguntas: "que pasa si borro esto?", "que pasa si cambio este numero?"

## Mensaje importante para principiantes

Equivocarse es normal. Ver errores en pantalla no significa que "no sirves para programar". Significa que estas probando, observando y aprendiendo.

En programacion, avanzar suele consistir en hacer pruebas pequeñas, leer con calma lo que aparece en pantalla y volver a intentar.
