# Informacion Personal

- Nombre: Camila Choque 
- Expectativas sobre la materia: Mayor entendimiento de software y del desarrollo web. 
- Intereses relacionados: IA, desarrollo web y ciberseguridad. 
- Hobbies: Leer,ver peliculas, entrenar.

# TP 1: "Sistema Concurrente de Análisis Biométrico con Cadena de Bloques Local"
## Descripción
- Este proyecto implementa un sistema distribuido en Python que simula la generación en tiempo real de datos biométricos de una prueba de esfuerzo y los procesa concurrentemente. Cada dato es analizado por procesos específicos, y los resultados se validan y almacenan en una cadena de bloques local para garantizar la integridad de los datos.
## Archivos
  - main.py — Código principal que ejecuta los procesos concurrentes.
  - frecuencia.py, presion.py, oxigeno.py — Procesos analizadores específicos.
  - verificador.py — Proceso verificador que construye la cadena de bloques.
  - verificar_cadena.py — Script externo para validar la cadena de bloques y generar reporte.
  - blockchain.json — Archivo donde se almacena la cadena de bloques (generado al correr main.py).
  - reporte.txt — Reporte generado por verificar_cadena.py.
## Pasos para ejecutar
- 1 . Clonar el repositorio
  -      git clone git@github.com:Camila-Choque/Compu2.git
  2 . Navegar hasta el directorio correspondiente
  -     cd TP_1
  3 . Instalar las dependencias (si no las tenés):
  -     pip install numpy
    otra opcion es:
  -     sudo apt install python3-numpy
  4 . Ejecutar el sistema concurrente para generar la cadena de bloques (se genera el archivo "blockchain.json"):
  -     python3 main.py
  5 . Ejecutar el script externo para verificar la cadena y generar reporte (se genera el archivo "reporte.txt"):
  -     python3 verificar_cadena.py




     

