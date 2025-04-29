import threading

def leer():
    with open("fifo_a_b", "r") as fifo:
        while True:
            mensaje = fifo.readline()
            if mensaje:
                print(f"[Usuario A]: {mensaje.strip()}")

def escribir():
    with open("fifo_b_a", "w") as fifo:
        while True:
            mensaje = input("[Vos]: ")
            fifo.write(mensaje + "\n")
            fifo.flush()

threading.Thread(target=leer, daemon=True).start()
escribir()
