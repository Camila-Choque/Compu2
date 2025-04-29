import signal
import os
import time

def manejador_sigusr1(signum, frame):
    print("¡Recibí SIGUSR1!")

signal.signal(signal.SIGUSR1, manejador_sigusr1)

print(f"Esperando SIGUSR1... PID = {os.getpid()}")
while True:
    time.sleep(1)
