# escritor_fifo.py
import os
import time

fifo_path = "fifo_cursor"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open(fifo_path, 'w') as fifo:
    for i in range(5):
        mensaje = f"Mensaje {i}\n"
        print(f"[Escritor] Enviando: {mensaje.strip()}")
        fifo.write(mensaje)
        fifo.flush()
        time.sleep(1)
