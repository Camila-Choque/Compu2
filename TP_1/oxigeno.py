import numpy as np

def analizador_oxigeno(pipe, queue):
    ventana = []

    while True:
        try:
            data = pipe.recv()
        except EOFError:
            break

        oxigeno = data["oxigeno"]
        ventana.append(oxigeno)

        if len(ventana) > 30:
            ventana.pop(0)

        media = np.mean(ventana)
        desv = np.std(ventana)

        resultado = {
            "tipo": "oxigeno",
            "timestamp": data["timestamp"],
            "media": media,
            "desv": desv
        }

        queue.put(resultado)
