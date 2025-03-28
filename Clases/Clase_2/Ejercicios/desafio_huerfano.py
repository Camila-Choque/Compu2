""""
5.4 Ejercicio 4: Crear un proceso huérfano
📌 Objetivo: Hacer que un proceso hijo viva más que su padre y verificar que su nuevo padre
 sea init/systemd (PID 1)."
"""
import os
import time 

pid = os.fork()

if pid > 0:
    print(f"Padre: Mi PID es {os.getpid()}")
    exit(0)  
else:
    time.sleep(10) #El hijo sigue vivo
    print("Hijo:Ahora soy un proceso huerfano")
   
