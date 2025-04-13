""""
Objetivo del ejercicio:

Simular un chat simple entre dos procesos (A y B), donde ambos pueden enviarse mensajes
 en ambas direcciones.
1. Cómo funciona:

    Proceso A enviará un mensaje a Proceso B.

    Proceso B recibirá el mensaje, lo procesará y luego lo enviará de vuelta a Proceso A.

    Este proceso se repetirá varias veces, simulando una conversación entre los dos 
    procesos.

2. Conceptos que vamos a usar:

    Pipes bidireccionales: Dos pipes, uno para cada dirección de comunicación.

    Procesos en paralelo: Usamos el módulo multiprocessing para crear dos procesos 
    que se comuniquen entre sí."
"""
from multiprocessing import Process, Pipe
import time

def proceso_a(pipe_a, pipe_b):
    """Proceso A: Envía un mensaje a B y espera una respuesta"""
    for i in range(3):
        mensaje = f"Mensaje de A, iteración {i+1}"
        print(f"A enviando: {mensaje}")
        pipe_a.send(mensaje)  # Enviar mensaje a B
        respuesta = pipe_b.recv()  # Esperar respuesta de B
        print(f"A recibió: {respuesta}")
        time.sleep(1)  # Simular procesamiento

def proceso_b(pipe_a, pipe_b):
    """Proceso B: Recibe mensaje de A, responde y lo envía de vuelta"""
    for i in range(3):
        mensaje = pipe_a.recv()  # Recibir mensaje de A
        print(f"B recibió: {mensaje}")
        respuesta = f"Respuesta de B, iteración {i+1}"
        print(f"B enviando: {respuesta}")
        pipe_b.send(respuesta)  # Enviar respuesta a A
        time.sleep(1)  # Simular procesamiento

if __name__ == '__main__':
    # Crear pipes
    pipe_a, pipe_b = Pipe()  # Pipe de A a B
    pipe_c, pipe_d = Pipe()  # Pipe de B a A

    # Crear procesos
    p_a = Process(target=proceso_a, args=(pipe_a, pipe_d))  # Proceso A
    p_b = Process(target=proceso_b, args=(pipe_b, pipe_c))  # Proceso B

    # Iniciar procesos
    p_a.start()
    p_b.start()

    # Esperar a que los procesos terminen
    p_a.join()
    p_b.join()
