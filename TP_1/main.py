import multiprocessing
from generador import generador
from frecuencia import analizador_frecuencia
from presion import analizador_presion
from oxigeno import analizador_oxigeno
from verificador import verificador

if __name__ == "__main__":
    
    a_pipe_parent, a_pipe_child = multiprocessing.Pipe()
    b_pipe_parent, b_pipe_child = multiprocessing.Pipe()
    c_pipe_parent, c_pipe_child = multiprocessing.Pipe()

   
    cola_resultados = multiprocessing.Queue()

    # Procesos analizadores
    proc_a = multiprocessing.Process(target=analizador_frecuencia, args=(a_pipe_child, cola_resultados))
    proc_b = multiprocessing.Process(target=analizador_presion, args=(b_pipe_child, cola_resultados))
    proc_c = multiprocessing.Process(target=analizador_oxigeno, args=(c_pipe_child, cola_resultados))

    # Proceso verificador
    proc_verif = multiprocessing.Process(target=verificador, args=(cola_resultados,))

    # Proceso generador
    proc_gen = multiprocessing.Process(target=generador, args=(a_pipe_parent, b_pipe_parent, c_pipe_parent))

    # Iniciar procesos
    proc_a.start()
    proc_b.start()
    proc_c.start()
    proc_verif.start()
    proc_gen.start()

    try:
        proc_gen.join()
    except KeyboardInterrupt:
        print("\n[!] Interrupción detectada. Finalizando procesos...")

       
        a_pipe_parent.close()
        b_pipe_parent.close()
        c_pipe_parent.close()

       
        proc_a.join()
        proc_b.join()
        proc_c.join()

        
        cola_resultados.put("FIN")
        proc_verif.join()
