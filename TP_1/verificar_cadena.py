import json
import hashlib

def calcular_hash(prev_hash, datos, timestamp):
    cadena = prev_hash + str(datos) + timestamp
    return hashlib.sha256(cadena.encode('utf-8')).hexdigest()

def verificar_blockchain():
    with open("blockchain.json", "r") as f:
        bloques = json.load(f)

    bloques_corruptos = []
    alertas = 0
    suma_frecuencia = 0
    suma_presion_sis = 0
    suma_presion_dia = 0
    suma_oxigeno = 0

    for i, bloque in enumerate(bloques):
        # Verificar encadenamiento
        if i == 0:
            esperado_prev_hash = "0"
        else:
            esperado_prev_hash = bloques[i-1]["hash"]

        if bloque["prev_hash"] != esperado_prev_hash:
            bloques_corruptos.append(i)

        # Recalcular hash
        hash_calculado = calcular_hash(bloque["prev_hash"], bloque["datos"], bloque["timestamp"])
        if hash_calculado != bloque["hash"]:
            bloques_corruptos.append(i)

        # Contar alertas
        if bloque.get("alerta", False):
            alertas += 1

        # Sumar para promedios
        datos = bloque["datos"]
        suma_frecuencia += datos["frecuencia"]["media"]
        suma_presion_sis += datos["presion"]["media"][0]
        suma_presion_dia += datos["presion"]["media"][1]
        suma_oxigeno += datos["oxigeno"]["media"]

    total = len(bloques)
    if total > 0:
        promedio_frecuencia = suma_frecuencia / total
        promedio_presion_sis = suma_presion_sis / total
        promedio_presion_dia = suma_presion_dia / total
        promedio_oxigeno = suma_oxigeno / total
    else:
        promedio_frecuencia = promedio_presion_sis = promedio_presion_dia = promedio_oxigeno = 0

    # Crear reporte
    with open("reporte.txt", "w") as f:
        f.write(f"Cantidad total de bloques: {total}\n")
        f.write(f"Número de bloques con alertas: {alertas}\n")
        f.write(f"Bloques corruptos encontrados: {bloques_corruptos if bloques_corruptos else 'Ninguno'}\n")
        f.write("Promedio general:\n")
        f.write(f"  Frecuencia: {promedio_frecuencia:.2f}\n")
        f.write(f"  Presión sistólica: {promedio_presion_sis:.2f}\n")
        f.write(f"  Presión diastólica: {promedio_presion_dia:.2f}\n")
        f.write(f"  Oxígeno: {promedio_oxigeno:.2f}\n")

    print("Verificación completada. Reporte generado en reporte.txt")

if __name__ == "__main__":
    verificar_blockchain()
