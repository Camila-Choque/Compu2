import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch, AsyncMock
from aiohttp import web
from server_scraping import handle_scrape_request, health_check, perform_scraping, send_to_processing_server

class TestServerScraping(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Crea una app simulada de aiohttp
        self.app = web.Application()
        self.app.router.add_get('/scrape', handle_scrape_request)
        self.app.router.add_post('/scrape', handle_scrape_request)
        self.app.router.add_get('/health', health_check)
        self.client = await self.get_client(self.app)

    async def get_client(self, app):
        from aiohttp.test_utils import TestClient, TestServer
        server = TestServer(app)
        await server.start_server()
        return TestClient(server)

    async def asyncTearDown(self):
        await self.client.close()

    # ---------- TEST 1: health_check ----------
    async def test_health_check(self):
        resp = await self.client.get('/health')
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertEqual(data["status"], "ok")

    # ---------- TEST 2: handle_scrape_request sin URL ----------
    async def test_scrape_missing_url(self):
        resp = await self.client.get('/scrape')
        self.assertEqual(resp.status, 400)
        data = await resp.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'URL parameter is required')

    # ---------- TEST 3: handle_scrape_request con URL válida ----------
    @patch("server_scraping.perform_scraping", new_callable=AsyncMock)
    async def test_scrape_with_valid_url(self, mock_scrape):
        mock_scrape.return_value = {
            "url": "http://example.com",
            "status": "success",
            "scraping_data": {"title": "Example"},
            "processing_data": {},
        }
        resp = await self.client.get('/scrape?url=http://example.com')
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertEqual(data["status"], "success")
        mock_scrape.assert_awaited_once()

    # ---------- TEST 4: perform_scraping (éxito) ----------
    @patch("server_scraping.fetch_html", new_callable=AsyncMock)
    @patch("server_scraping.send_to_processing_server", new_callable=AsyncMock)
    @patch("server_scraping.extract_title", return_value="Título de prueba")
    @patch("server_scraping.extract_links", return_value=["link1", "link2"])
    @patch("server_scraping.extract_meta_tags", return_value={"author": "test"})
    @patch("server_scraping.count_headers", return_value={"h1": 1})
    @patch("server_scraping.count_images", return_value=3)
    async def test_perform_scraping_success(
        self, mock_images, mock_headers, mock_meta, mock_links, mock_title, mock_processing, mock_fetch
    ):
        mock_fetch.return_value = "<html><title>Test</title></html>"
        mock_processing.return_value = {"processing_data": {"ok": True}}
        result = await perform_scraping("http://example.com")
        self.assertEqual(result["status"], "success")
        self.assertIn("scraping_data", result)
        self.assertIn("processing_data", result)
        mock_processing.assert_awaited_once()

    # ---------- TEST 5: perform_scraping (error) ----------
    @patch("server_scraping.fetch_html", new_callable=AsyncMock, side_effect=Exception("Falla de red"))
    async def test_perform_scraping_error(self, mock_fetch):
        result = await perform_scraping("http://example.com")
        self.assertEqual(result["status"], "error")
        self.assertIn("error", result)

    # ---------- TEST 6: send_to_processing_server (error) ----------
    @patch("server_scraping.asyncio.open_connection", side_effect=Exception("conexión rechazada"))
    async def test_send_to_processing_server_error(self, mock_conn):
        result = await send_to_processing_server({"url": "http://example.com"})
        self.assertEqual(result["status"], "error")
        self.assertIn("processing_data", result)
        self.assertEqual(result["processing_data"]["performance"]["load_time_ms"], 0)


if __name__ == "__main__":
    unittest.main()
