import numpy as np

def analizador_frecuencia(pipe, queue):
    import numpy as np
    ventana = []

    try:
        while True:
            try:
                data = pipe.recv()
            except EOFError:
                break  

            frecuencia = data["frecuencia"]
            ventana.append(frecuencia)
            if len(ventana) > 30:
                ventana.pop(0)  

            media = np.mean(ventana)
            desv = np.std(ventana)

            resultado = {
                "tipo": "frecuencia",
                "timestamp": data["timestamp"],
                "media": media,
                "desv": desv
            }

            queue.put(resultado)
    except KeyboardInterrupt:
        pass

