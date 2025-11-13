import json

def serialize_result(data: dict) -> bytes:
    """Serializa un diccionario a bytes usando JSON."""
    return json.dumps(data, ensure_ascii=False).encode('utf-8')

def deserialize_result(data: bytes) -> dict:
    """Deserializa bytes a un diccionario usando JSON."""
    return json.loads(data.decode('utf-8'))
