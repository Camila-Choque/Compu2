""""
"Avancemos con el desafío práctico:

Ahora, te propongo que combines los tres ejercicios anteriores en un único script. El script debe aceptar los siguientes argumentos:

    -n o --nombre_archivo: Un nombre de archivo (tipo str).

    -v o --verbose: Un modo detallado que active un mensaje adicional.

    -n o --numero: Un número que se multiplicará por 2."
"""
import argparse

# Crear el parser
parser = argparse.ArgumentParser()

# Definir el argumento para el nombre del archivo
parser.add_argument("-n", "--nombre_archivo", type=str, help="Nombre del archivo", required=True)

# Definir el argumento para el modo detallado
parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")

# Definir el argumento para el número a multiplicar
parser.add_argument("-m", "--numero", type=int, help="Número a multiplicar por 2")

# Parsear los argumentos
args = parser.parse_args()

# Mostrar el nombre del archivo
print(f"Nombre del archivo: {args.nombre_archivo}")

# Si el modo detallado está activado, mostrar mensaje adicional
if args.verbose:
    print("Procesando archivo en modo detallado")

# Si el número fue pasado, hacer la multiplicación
if args.numero is not None:
    resultado = args.numero * 2
    print(f"Resultado de la multiplicación: {resultado}")
else:
    print("No se proporcionó un número para multiplicar.")

""""
Ejecutar el script con el nombre del archivo:
python3 script_argparse_2.py -n archivo.txt

Ejecutar el script con el nombre del archivo y el modo detallado:
python3 script_argparse_2.py -n archivo.txt -v

Ejecutar el script con el nombre del archivo y un número para multiplicar:
python3 script_argparse_2.py -n archivo.txt -m 5

Ejecutar el script con todos los argumentos (nombre del archivo, modo detallado, número):
python3 script_argparse_2.py -n archivo.txt -v -m 5

"""