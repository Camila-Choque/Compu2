#🧩 Ejercicio 1: Varios productores, un consumidor
#Objetivo: tener dos procesos que generan datos y un solo proceso que los consume.

from multiprocessing import Process, Queue
import time
import random

def productor(nombre, q):
    for i in range(5):
        valor = f"{nombre}-{i}"
        print(f"[{nombre}] Generando: {valor}")
        q.put(valor)
        time.sleep(random.uniform(0.2, 0.6))

def consumidor(q, total_datos):
    for _ in range(total_datos):
        dato = q.get()
        print(f"[Consumidor] Recibido: {dato}")

if __name__ == "__main__":
    cola = Queue()
    total_datos = 10  # 5 de cada productor
    p1 = Process(target=productor, args=("Productor1", cola))
    p2 = Process(target=productor, args=("Productor2", cola))
    c = Process(target=consumidor, args=(cola, total_datos))

    p1.start()
    p2.start()
    c.start()

    p1.join()
    p2.join()
    c.join()

    print("Múltiples productores y un consumidor finalizado.")
