import signal
import os
import time

# Paso 1: definir el manejador
def manejador_sigint(signum, frame):
    print(f"[{os.getpid()}] ¡Señal SIGINT recibida! (signum={signum})")

# Paso 2: registrar el manejador
signal.signal(signal.SIGINT, manejador_sigint)

# Paso 3: mostrar el PID del proceso
print(f"PID del proceso: {os.getpid()}")
print("Esperando señales... presioná Ctrl+C o usá kill -SIGINT PID")

# Paso 4: bucle que espera señales
while True:
    time.sleep(1)
