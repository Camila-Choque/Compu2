import aiohttp
import time

async def measure_performance(url: str) -> dict:
    try:
        start_time = time.time()

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                load_time_ms = int((time.time() - start_time) * 1000)
                content = await response.read()
                total_size_kb = len(content) / 1024
                num_requests = 1

                return {
                    "load_time_ms": load_time_ms,
                    "total_size_kb": round(total_size_kb, 2),
                    "num_requests": num_requests
                }

    except Exception as e:
        print(f" Error midiendo rendimiento: {e}")
        return {
            "load_time_ms": 0,
            "total_size_kb": 0,
            "num_requests": 0
        }






