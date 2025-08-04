import numpy as np
#sudo apt install python3-pip
def analizador_frecuencia(pipe, queue):
    ventana = []

    while True:
        try:
            data = pipe.recv()
        except EOFError:
            break  # Pipe cerrado, fin de datos

        frecuencia = data["frecuencia"]
        ventana.append(frecuencia)
        if len(ventana) > 30:
            ventana.pop(0)  # mantener ventana móvil

        media = np.mean(ventana)
        desv = np.std(ventana)

        resultado = {
            "tipo": "frecuencia",
            "timestamp": data["timestamp"],
            "media": media,
            "desv": desv
        }

        queue.put(resultado)
