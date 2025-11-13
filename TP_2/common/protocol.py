
import json
import struct

def encode_message(data: dict) -> bytes:
    payload = json.dumps(data).encode("utf-8")
    header = struct.pack("!I", len(payload))   
    return header + payload


def decode_message(sock) -> dict:
    header = sock.recv(4)
    if not header:
        raise ConnectionError("Conexión cerrada")

    (length,) = struct.unpack("!I", header)
    payload = b""
    while len(payload) < length:
        chunk = sock.recv(length - len(payload))
        if not chunk:
            raise ConnectionError("Conexión cerrada durante lectura")
        payload += chunk


    return json.loads(payload.decode("utf-8"))


# Estructuras de mensajes 
def request_processing(task_type: str, data: dict) -> dict:
    """
    Crea un mensaje estándar para pedirle al Servidor B que procese algo.
    """
    return {
        "type": "PROCESS_REQUEST",
        "task": task_type,   # "screenshot", "performance", "images"
        "data": data
    }


def response_ok(result: dict) -> dict:
    """
    Respuesta exitosa del servidor B.
    """
    return {
        "type": "PROCESS_RESPONSE",
        "status": "OK",
        "result": result
    }


def response_error(message: str) -> dict:
    """
    Respuesta de error estándar.
    """
    return {
        "type": "PROCESS_RESPONSE",
        "status": "ERROR",
        "error": message
    }
