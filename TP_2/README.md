# Informacion del Alumno

- Nombre y Apellido: Choque Camila
- Legajo: 62069
- Correo: m.choque@alumno.um.edu.ar

# TP2 - Sistema de Scraping y Análisis Web Distribuido

# Descripcion 
- Se requiere desarrollar un sistema distribuido de scraping y análisis web utilizando Python. El sistema debe consistir en dos servidores que trabajan de forma coordinada para extraer, analizar y procesar información de sitios web.

# Estructura del Proyecto 
| Archivo / Carpeta          | Descripción                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| `server_scraping.py`       | Servidor asíncrono (Parte A)                                                |
| `server_processing.py`     | Servidor multiproceso (Parte B)                                             |
| `client.py`                | Cliente que envía solicitudes de scraping y procesamiento                   |
| **scraper/**               | Módulo con la lógica de scraping                                            |
| ├─ `__init__.py`           | Inicializa el módulo `scraper`                                              |
| ├─ `html_parser.py`        | Funciones para extraer títulos, enlaces, imágenes y encabezados del HTML    |
| ├─ `metadata_extractor.py` | Extracción de metadatos (meta tags, descripciones, palabras clave, etc.)    |
| └─ `async_http.py`         | Cliente HTTP asíncrono que obtiene el contenido HTML                        |
| **processor/**             | Módulo con las operaciones de procesamiento                                 |
| ├─ `__init__.py`           | Inicializa el módulo `processor`                                            |
| ├─ `screenshot.py`         | Captura de pantallas de las páginas (screenshots)                           |
| ├─ `performance.py`        | Medición de rendimiento: tiempos de carga, tamaño total, número de requests |
| └─ `image_processor.py`    | Procesamiento y manipulación de imágenes generadas                          |
| **common/**                | Módulo compartido por ambos servidores                                      |
| ├─ `__init__.py`           | Inicializa el módulo `common`                                               |
| ├─ `protocol.py`           | Definición del protocolo de comunicación entre Servidor A y B               |
| └─ `serialization.py`      | Serialización y deserialización de datos usando JSON                        |
| **tests/**                 | Conjunto de pruebas unitarias                                               |
| ├─ `test_scraper.py`       | Pruebas del servidor de scraping (Parte A)                                  |
| └─ `test_processor.py`     | Pruebas del servidor de procesamiento (Parte B)                             |
| `requirements.txt`         | Dependencias necesarias para ejecutar el proyecto                           |
| `README.md`                | Documentación general del proyecto                                          |

# Ejecucion Principal

### 1 - Clonar repositorio
       git clone git@github.com:Camila-Choque/Compu2.git
### 2 - Navegar al directorio
     cd Compu2/TP_2
### 3- Crear el entorno virtual
     python3 -m venv .venv
### 4 - Activarlo
     source .venv/bin/activate 
### 5 - Instalar dependencias
     pip install -r requirements.txt 
### 6 - (Opcional) Instalar Google Chrome en Ubuntu/Debian
     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
     sudo dpkg -i google-chrome-stable_current_amd64.deb
     sudo apt-get install -f

# Ejecucion de Servidores

### 1 - En una terminal adentro del entorno virtual activar el servidor de scraping (Parte A):
     python server_scraping.py -i 0.0.0.0 -p 8000
### 2 - En una segunda terminal adentro del entorno virtual instalamos lo siguiente:
     pip install webdriver-manager
### Luego activamos el servidor de procesamiento (Parte B):
     python server_processing.py -i 0.0.0.0 -p 9001 -n 4
### 3 - En una tercera terminal adentro del entorno virtual ejecutar el siguiente comando:
    python3 client.py

- Nota: Como resultado final, el scraper devuelve un JSON con toda la información extraída de la página web. Además, se abre automáticamente una pestaña (o se puede visualizar en los archivos) mostrando una captura de la página.

# Ejecucion de Test
### 1- Para ejecutar test_processor.py se debe estar dentro del entorno virtual:
    python3 Test/test_processor.py
### 2- Para ejecutar test_scraper.py se debe estar dentro del entorno virtual:
    python3 Test/test_scraper.py
