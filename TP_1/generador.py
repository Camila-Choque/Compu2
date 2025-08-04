import multiprocessing
import time
import random
from datetime import datetime

def generador(pipe_a, pipe_b, pipe_c):
    for _ in range(60):  # 60 muestras, 1 por segundo
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "frecuencia": random.randint(60, 180),
            "presion": [random.randint(110, 180), random.randint(70, 110)],
            "oxigeno": random.randint(90, 100)
        }
        
        pipe_a.send(data)
        pipe_b.send(data)
        pipe_c.send(data)

        time.sleep(1)  # esperar 1 segundo

    # Luego de enviar los 60 datos
    pipe_a.close()
    pipe_b.close()
    pipe_c.close()
