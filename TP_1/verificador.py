import hashlib
import json

def calcular_hash(prev_hash, datos, timestamp):
    datos_str = json.dumps(datos, sort_keys=True)
    cadena = prev_hash + datos_str + timestamp
    return hashlib.sha256(cadena.encode('utf-8')).hexdigest()


def verificador(queue):
    bloques = []
    pendientes = {}
    prev_hash = "0"  

    while True:
        resultado = queue.get()
        if resultado == "FIN":
            break

        ts = resultado["timestamp"]
        tipo = resultado["tipo"]

        if ts not in pendientes:
            pendientes[ts] = {}

        pendientes[ts][tipo] = {
            "media": resultado["media"],
            "desv": resultado["desv"]
        }

        if len(pendientes[ts]) == 3:
            datos = pendientes.pop(ts)

            freq = datos["frecuencia"]["media"]
            oxi = datos["oxigeno"]["media"]
            presion_sistolica = datos["presion"]["media"][0] if isinstance(datos["presion"]["media"], (list, tuple)) else datos["presion"]["media"]

            alerta = bool(
            freq >= 200 or
             oxi < 90 or oxi > 100 or
            presion_sistolica >= 200
            )


            bloque = {
                "timestamp": ts,
                "datos": datos,
                "alerta": alerta,
                "prev_hash": prev_hash,
            }

            bloque["hash"] = calcular_hash(prev_hash, datos, ts)
            prev_hash = bloque["hash"]
            bloques.append(bloque)

            try:
                with open("blockchain.json", "w") as f:
                    json.dump(bloques, f, indent=4)
                    f.flush()
                print(f"Bloque #{len(bloques)-1} guardado. Hash: {bloque['hash']} | ALERTA: {alerta}")
            except Exception as e:
                print("Error guardando blockchain.json:", e)
