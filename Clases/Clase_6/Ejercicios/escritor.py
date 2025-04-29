import time
import os

with open("log_fifo", "w") as fifo:
    for i in range(5):
        mensaje = f"PID {os.getpid()} - Mensaje {i}"
        fifo.write(mensaje + "\n")
        fifo.flush()
        time.sleep(1)
