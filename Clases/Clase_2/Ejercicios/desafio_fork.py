""""
"📌 Objetivo: Crear un proceso hijo con fork(), hacer que imprima su PID y que el padre 
espere su finalización con wait()."
"""

import os
import time 

pid = os.fork()

if pid == 0:
    print(f"Hijo: Mi PID es {os.getpid()}")
    exit(0)  # El hijo termina/evita que se siga ejecutando el padre
else:
    os.wait()
    time.sleep(5)  # Para evitar que el shell termine antes de verificar
    print(f"Padre: Mi hijo {pid} terminó.")
