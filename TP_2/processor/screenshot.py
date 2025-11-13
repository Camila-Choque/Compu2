from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
import io
from PIL import Image

def capture_screenshot(url: str) -> str:
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")

       
        options.binary_location = "/usr/bin/google-chrome"  

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)

        screenshot_png = driver.get_screenshot_as_png()

        img = Image.open(io.BytesIO(screenshot_png))
        img.thumbnail((1280, 720), Image.Resampling.LANCZOS)

        buffer = io.BytesIO()
        img.save(buffer, format='PNG', optimize=True)
        screenshot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return screenshot_base64

    except Exception as e:
        print(f" Error al generar el screenshot: {e}")
        return None
    finally:
        if 'driver' in locals():
            driver.quit()
