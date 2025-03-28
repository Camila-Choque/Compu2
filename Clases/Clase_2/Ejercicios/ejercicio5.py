#Ejercicio 5: Proceso zombi temporal

import os, time

pid = os.fork()
if pid == 0:
    print("[HIJO] Finalizando")
    os._exit(0)
else:
    print("[PADRE] No llamaré a wait() aún. Observa el zombi con 'ps -el'")
    time.sleep(15)
    os.wait()
