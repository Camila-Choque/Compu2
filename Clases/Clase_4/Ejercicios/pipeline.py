"""
🔧 Ejercicio 1 – Pipeline de 3 procesos con multiprocessing.Pipe
🎯 Objetivo:

Simular este flujo de comunicación:

Proceso A → Proceso B → Proceso C

    A genera un número.

    B recibe ese número y lo multiplica por 2.

    C recibe el resultado final y lo imprime."
"""

from multiprocessing import Process, Pipe

def proceso_a(envio):
    numero = 5
    print("Genero el numero", numero )

    envio.send(numero)
    envio.close()

def proceso_b(recibo, envio_b):

    numero = recibo.recv()
    print("El numero recibido es ", numero)
    cuenta = numero * 2
    print("El numero del proceso B es ", cuenta)
    envio_b.send(cuenta)
    envio_b.close()

def proceso_c(recibo_b):

    numero = recibo_b.recv()

    print("El resultado final es", numero)

if __name__ == "__main__":
    # Pipe entre A y B
    a_b_padre, a_b_hijo = Pipe()
    # Pipe entre B y C
    b_c_padre, b_c_hijo = Pipe()

    # Crear procesos
    a = Process(target=proceso_a, args=(a_b_padre,))
    b = Process(target=proceso_b, args=(a_b_hijo, b_c_padre))
    c = Process(target=proceso_c, args=(b_c_hijo,))

    # Iniciar procesos
    a.start()
    b.start()
    c.start()

    # Esperar que terminen
    a.join()
    b.join()
    c.join()