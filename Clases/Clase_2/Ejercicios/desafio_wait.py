""" "
5.3 Ejercicio 2: Detectar un proceso zombi
📌 Objetivo: Crear un proceso hijo que termine rápido, pero hacer que el padre no llame wait(),
 generando un zombi."
"""
import os
import time 

pid = os.fork()

if pid == 0:
    print(f"Hijo: Mi PID es {os.getpid()}")
    os.exit(0)  # El hijo termina/evita que se siga ejecutando el padre
else:
    print("Proceso zombi")
    time.sleep(10)  # El padre sigue vivo sin esperar al hijo
