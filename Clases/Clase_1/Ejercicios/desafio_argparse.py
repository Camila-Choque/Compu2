""""
📌 Desafío práctico:

Crea un script que:

    Acepte un argumento obligatorio -i o --input que sea el nombre de un archivo.

    Acepte un argumento opcional -v o --verbose que, si está presente, imprima un mensaje adicional, 
    como "Procesando archivo en modo detallado".

    Acepte un argumento -n o --numero que sea un número entero, y que imprima ese número multiplicado
    por 2.

"""

#PRIMERO------------------------------------------------------------------------------------------
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n","--nombre_archivo",type=str,help="Nombre_del_archivo",required=True) #Argumento obligatorio

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
print(f"Nombre del archivo: {args.nombre_archivo}.")

#SEGUNDO---------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument("-v","--verbose",action="store_true",help="Modo detallado")

args = parser.parse_args()

if args.verbose:
    print("Proceso archivo en modo detallado")
else:
    print("Nada que decir ")

#TERCERO--------------------------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument("-l","--numero",type=int,help="Multiplicacion")

args = parser.parse_args()

# Verificar si se proporcionó el número
if args.numero is not None:
    args.cuenta = args.numero * 2
    print(f"Operación: {args.cuenta}")
else:
    print("No se proporcionó un número para multiplicar.")

