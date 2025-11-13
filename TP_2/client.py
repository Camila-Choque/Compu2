import aiohttp
import asyncio
import json
import base64
from PIL import Image
import io

SERVER_URL = "http://127.0.0.1:8000/scrape?url=https://www.google.com"

async def main():
    url = "https://www.google.com"
    print(f"--- Prueba Avanzada: Analizando {url} ---")
    print("[*] (Esto puede tardar unos segundos...)")

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(SERVER_URL, params={"url": url}) as response:
                if response.status == 200:
                    data = await response.json()
                    print("\n--- JSON Recibido del Servidor A: ---")
                    print(json.dumps(data, indent=2, ensure_ascii=False))

                    
                    if data.get("processing_data", {}).get("screenshot"):
                        screenshot_base64 = data["processing_data"]["screenshot"]
                        screenshot_data = base64.b64decode(screenshot_base64)
                        screenshot_image = Image.open(io.BytesIO(screenshot_data))
                        screenshot_image.save("screenshot.png")
                        screenshot_image.show()  
                else:
                    print(f"❌ Error en la respuesta del servidor: {response.status}")
                    print(await response.text())

        except aiohttp.ClientError as e:
            print(f"❌ Error al conectar con el servidor: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    asyncio.run(main())


