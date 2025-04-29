with open("log_fifo", "r") as fifo:
    print("🟢 Lector de logs iniciado. Esperando mensajes...")
    while True:
        linea = fifo.readline()
        if linea:
            print(f"[LOG] {linea.strip()}")
