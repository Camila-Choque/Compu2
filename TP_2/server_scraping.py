import asyncio
import argparse
from datetime import datetime, UTC
from aiohttp import web
from bs4 import BeautifulSoup
from scraper.async_http import fetch_html
from scraper.html_parser import extract_title, extract_links, count_images, count_headers
from scraper.metadata_extractor import extract_meta_tags
from common.serialization import serialize_result, deserialize_result

PROCESSING_HOST = "127.0.0.1" 
PROCESSING_PORT = 9001

async def send_to_processing_server(payload: dict):
    try:
        reader, writer = await asyncio.open_connection(PROCESSING_HOST, PROCESSING_PORT)
        serialized = serialize_result(payload)
        writer.write(len(serialized).to_bytes(4, "big") + serialized)
        await writer.drain()

        resp_length_bytes = await reader.readexactly(4)
        resp_length = int.from_bytes(resp_length_bytes, "big")
        resp_data = await reader.readexactly(resp_length)
        writer.close()
        await writer.wait_closed()

        return deserialize_result(resp_data)

    except Exception as e:
        #print(f"❌ Error comunicando con servidor de procesamiento: {e}")
        return {
            "processing_data": {
                "screenshot": "",
                "performance": {"load_time_ms": 0, "total_size_kb": 0, "num_requests": 0},
                "thumbnails": []
            },
            "status": "error",
            "error": str(e)
        }

async def perform_scraping(url: str):
    #print(f"🔍 Iniciando scraping de: {url}")
    try:
        html_text = await fetch_html(url)
        if not html_text:
            raise Exception("No se pudo obtener el HTML")

        soup_data = BeautifulSoup(html_text, "html.parser")
        scraping_result = {
            "title": extract_title(soup_data),
            "links": extract_links(soup_data, base_url=url),
            "meta_tags": extract_meta_tags(soup_data),
            "structure": count_headers(soup_data),
            "images_count": count_images(soup_data),
        }
        #print(f"✅ Scraping completado: {scraping_result['title']}")

        processing_payload = {"url": url, "html": html_text}
        processing_response = await send_to_processing_server(processing_payload)

        return {
            "url": url,
            "timestamp": datetime.now(UTC).isoformat() + "Z",
            "scraping_data": scraping_result,
            "processing_data": processing_response.get("processing_data", {}),
            "status": "success"
        }

    except Exception as e:
        #print(f"❌ Error en scraping: {e}")
        return {
            "url": url,
            "timestamp": datetime.now(UTC).isoformat() + "Z",
            "status": "error",
            "error": str(e)
        }

async def handle_scrape_request(request):
    try:
        if request.method == 'POST':
            data = await request.json()
            url = data.get('url')
        else:
            url = request.query.get('url')

        if not url:
            return web.json_response({'error': 'URL parameter is required'}, status=400)

        result = await perform_scraping(url)
        return web.json_response(result)

    except Exception as e:
        #print(f"❌ Error en handler: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def health_check(request):
    return web.json_response({'status': 'ok'})

def parse_args():
    parser = argparse.ArgumentParser(description='Servidor de Scraping Web Asíncrono')
    parser.add_argument('-i', '--ip', default='0.0.0.0', help='Dirección de escucha (soporta IPv4)')
    parser.add_argument('-p', '--port', type=int, default=8000, help='Puerto de escucha')
    return parser.parse_args()

def main(ip, port):
    app = web.Application()
    app.router.add_get('/scrape', handle_scrape_request)
    app.router.add_post('/scrape', handle_scrape_request)
    app.router.add_get('/health', health_check)

    print(f"✅ Servidor de Scraping (A) escuchando en {ip}:{port}")
    print(f"   Endpoints:")
    print(f"   - GET/POST /scrape?url=<URL>")
    print(f"   - GET /health")

    web.run_app(app, host=ip, port=port)

if __name__ == "__main__":
    args = parse_args()
    main(args.ip, args.port)
