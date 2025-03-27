""""
"🚀 Desafío práctico

Ahora te toca a ti. Crea un script en Python que:

✅ Use argparse para aceptar dos argumentos:

    -i o --input: Nombre de un archivo de entrada.

    -o o --output: Nombre de un archivo de salida."
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-e","--archivo_entrada",type=str,help="Archivo_de_entrada")
parser.add_argument("-s","--archivo_salida",type=str,help="Archivo_de_salida")

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
print(f"Archivo de entrada {args.archivo_entrada}, Archivo de salida {args.archivo_salida} .")


""""
MODOD DE EJECUCION
python3 script_argparse.py -e entrada.txt -s salida.txt
 
ESPERADO
Archivo de entrada entrada.txt, Archivo de salida salida.txt 
"""