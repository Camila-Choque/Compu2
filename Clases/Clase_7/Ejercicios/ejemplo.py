import signal
import time

# Handler para SIGINT
def manejador_sigint(signum, frame):
    print("\n🔔 ¡Recibí SIGINT (Ctrl+C)!")

# Asociar señal con handler
signal.signal(signal.SIGINT, manejador_sigint)

print("Esperando señales... presiona Ctrl+C para enviar SIGINT.")
while True:
    time.sleep(1)

"""
🛠️ Instrucciones prácticas paso a paso

    Abre una terminal.

    Ejecuta un programa simple en Python que se quede esperando (sleep o input()).

    Desde otra terminal, usa el comando kill -SIGINT <pid> para enviar una señal.

    Observa cómo el programa se interrumpe.

    Comando para saber el pid -->ps aux | grep python


"""