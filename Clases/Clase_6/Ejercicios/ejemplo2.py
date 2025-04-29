# lector1.py o lector2.py
import os
import time

fifo_path = "fifo_cursor"

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

with open(fifo_path, 'r') as fifo:
    print("[Lector] Esperando mensajes...")
    while True:
        linea = fifo.readline()
        if not linea:
            time.sleep(0.5)  # Evita CPU al 100%
            continue
        print(f"[Lector] Recibido: {linea.strip()}")
