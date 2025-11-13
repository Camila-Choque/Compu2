import aiohttp
from aiohttp import ClientTimeout

async def fetch_html(url: str) -> str:
    timeout = ClientTimeout(total=30)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise Exception(f"Error descargando {url}: HTTP {response.status}: {response.reason}")
