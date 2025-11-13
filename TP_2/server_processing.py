import socketserver
import json
import argparse
import asyncio
from processor.screenshot import capture_screenshot
from processor.performance import measure_performance
from common.serialization import serialize_result, deserialize_result

class ProcessingHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            # Leer longitud del mensaje
            length_bytes = self.request.recv(4)
            if len(length_bytes) < 4:
                raise Exception("Longitud del mensaje incompleta")

            msg_len = int.from_bytes(length_bytes, "big")

            # Leer contenido completo
            data = b""
            while len(data) < msg_len:
                packet = self.request.recv(msg_len - len(data))
                if not packet:
                    break
                data += packet

            if len(data) != msg_len:
                raise Exception("Mensaje incompleto")

            request = deserialize_result(data)

            url = request.get("url")
            html = request.get("html", "")

            if not url:
                raise Exception("URL no proporcionada en la solicitud")

            # Ejecutar tareas secuencialmente
            screenshot_b64 = capture_screenshot(url)
            performance_data = asyncio.run(measure_performance(url))

            response = {
                "processing_data": {
                    "screenshot": screenshot_b64,
                    "performance": performance_data,
                    "thumbnails": [screenshot_b64] if screenshot_b64 else []
                },
                "status": "success"
            }

            serialized_response = serialize_result(response)
            self.request.sendall(len(serialized_response).to_bytes(4, "big") + serialized_response)

        except json.JSONDecodeError as e:
          
            error_resp = serialize_result({
                "processing_data": {
                    "screenshot": "",
                    "performance": {"load_time_ms": 0, "total_size_kb": 0, "num_requests": 0},
                    "thumbnails": []
                },
                "status": "error",
                "error": f"Error de JSON: {str(e)}"
            })
            self.request.sendall(len(error_resp).to_bytes(4, "big") + error_resp)

        except Exception as e:
        
            error_resp = serialize_result({
                "processing_data": {
                    "screenshot": "",
                    "performance": {"load_time_ms": 0, "total_size_kb": 0, "num_requests": 0},
                    "thumbnails": []
                },
                "status": "error",
                "error": str(e)
            })
            self.request.sendall(len(error_resp).to_bytes(4, "big") + error_resp)

def parse_args():
    parser = argparse.ArgumentParser(description='Servidor de Procesamiento Distribuido')
    parser.add_argument('-i', '--ip', default='0.0.0.0', help='Dirección de escucha (soporta IPv4)')
    parser.add_argument('-p', '--port', type=int, default=9001, help='Puerto de escucha')
    parser.add_argument('-n', '--processes', type=int, default=4, help='Número de procesos en el pool')
    return parser.parse_args()

def main(ip, port, processes):
    with socketserver.TCPServer((ip, port), ProcessingHandler) as server:
        print(f"{'='*70}")
        print(f"✅ Servidor de Procesamiento (B) iniciado")
        print(f"{'='*70}")
        print(f"   Host: {ip}")
        print(f"   Puerto: {port}")
        print(f"   Esperando conexiones del Servidor A...")
        print(f"{'='*70}\n")
        server.serve_forever()

if __name__ == "__main__":
    args = parse_args()
    main(args.ip, args.port, args.processes)
