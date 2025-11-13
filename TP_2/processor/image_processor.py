from PIL import Image
import base64
import io
import requests
import tempfile
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def create_thumbnail(image_path: str) -> str:

    try:
        with Image.open(image_path) as img:
            img.thumbnail((200, 200))
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return img_str
    except Exception as e:
        print(f" Error generando thumbnail: {e}")
        return ""


def generate_thumbnails(url, max_images=5, timeout=10):
    
    thumbnails = []
    temp_files = []  
    
    try:
        # Obtener el HTML de la página
        response = requests.get(url, timeout=timeout)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar todas las imágenes
        images = soup.find_all('img', src=True)
        
        print(f" Encontradas {len(images)} imágenes, procesando hasta {max_images}...")
        
        # Procesar hasta max_images 
        for idx, img_tag in enumerate(images[:max_images]):
            try:
                img_url = img_tag['src']
                
                # Convertir URL relativa a absoluta
                if not img_url.startswith('http'):
                    img_url = urljoin(url, img_url)
                
                print(f" Descargando imagen {idx+1}/{min(max_images, len(images))}: {img_url[:60]}...")
                
                # Descargar la imagen
                img_response = requests.get(img_url, timeout=5)
                
                if img_response.status_code != 200:
                    print(f"    Error HTTP {img_response.status_code}")
                    continue
                
                # Guardar en archivo temporal
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                    tmp_file.write(img_response.content)
                    tmp_path = tmp_file.name
                    temp_files.append(tmp_path)
                
                # Usar tu función create_thumbnail
                thumbnail_base64 = create_thumbnail(tmp_path)
                
                if thumbnail_base64:
                    thumbnails.append(thumbnail_base64)
                    print(f"   Thumbnail {idx+1} generado correctamente")
                
            except requests.Timeout:
                print(f"     Timeout descargando imagen {idx+1}")
                continue
            except Exception as e:
                print(f"     Error procesando imagen {idx+1}: {e}")
                continue
        
        print(f" {len(thumbnails)} thumbnails generados exitosamente")
        return thumbnails
        
    except Exception as e:
        print(f" Error generando thumbnails: {e}")
        return []
    
    finally:
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except Exception as e:
                print(f"  No se pudo eliminar archivo temporal {temp_file}: {e}")