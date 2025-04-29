import threading

def leer():
    with open("fifo_b_a", "r") as fifo:
        while True:
            mensaje = fifo.readline()
            if mensaje:
                print(f"[Usuario B]: {mensaje.strip()}")

def escribir():
    with open("fifo_a_b", "w") as fifo:
        while True:
            mensaje = input("[Vos]: ")
            fifo.write(mensaje + "\n")
            fifo.flush()

# Hilos: uno lee y otro escribe al mismo tiempo
threading.Thread(target=leer, daemon=True).start()
escribir()
