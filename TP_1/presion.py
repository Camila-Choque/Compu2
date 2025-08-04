import numpy as np

def analizador_presion(pipe, queue):
    ventana_sistolica = []
    ventana_diastolica = []

    while True:
        try:
            data = pipe.recv()
        except EOFError:
            break

        sistolica, diastolica = data["presion"]
        ventana_sistolica.append(sistolica)
        ventana_diastolica.append(diastolica)

        if len(ventana_sistolica) > 30:
            ventana_sistolica.pop(0)
            ventana_diastolica.pop(0)

        media = [np.mean(ventana_sistolica), np.mean(ventana_diastolica)]
        desv = [np.std(ventana_sistolica), np.std(ventana_diastolica)]

        resultado = {
            "tipo": "presion",
            "timestamp": data["timestamp"],
            "media": media,
            "desv": desv
        }

        queue.put(resultado)
