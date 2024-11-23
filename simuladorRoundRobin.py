from time import sleep
from itertools import cycle

# Colores para los procesos (código ANSI)
COLORES = [
    "\033[91m",  # Rojo
    "\033[92m",  # Verde
    "\033[93m",  # Amarillo
    "\033[94m",  # Azul
    "\033[95m",  # Magenta
    "\033[96m",  # Cian
    "\033[97m",  # Blanco
]
RESET_COLOR = "\033[0m"

class Proceso:
    def __init__(self, id, inicio, duracion):
        self.id = id
        self.inicio = inicio
        self.duracion = duracion
        self.tiempo_restante = duracion
        self.tiempo_espera = 0
        self.tiempo_final = 0
        self.tiempo_servicio = 0  # Calculado como tiempo_final - tiempo_primer_uso
        self.tiempo_primer_uso = None  # Momento en que el proceso entra al procesador por primera vez

def imprimir_barra(tiempo, proceso_id, cola):
    """Imprime una barra de progreso para el procesador y la cola de espera."""
    colores = cycle(COLORES)
    color = next(colores) if proceso_id != "No hay nada" else RESET_COLOR
    barra = f"{color}Tiempo {tiempo:2d}: {'P' + str(proceso_id) if proceso_id != 'No hay nada' else 'No hay nada'}{RESET_COLOR}"
    print(barra)

    if cola:
        cola_texto = "Cola de espera: " + ", ".join(f"P{p.id}" for p in cola)
    else:
        cola_texto = "Cola de espera: vacía"
    print(cola_texto)

def imprimir_barra_final(log_procesador):
    """Imprime una barra final mostrando cómo se ejecutaron los procesos."""
    print("\nEjecución final (barra de procesos):")
    colores = {f"P{idx + 1}": color for idx, color in enumerate(COLORES)}
    barra_final = ""
    for proceso in log_procesador:
        if proceso == "No hay nada":
            barra_final += "No hay nada "
        else:
            color = colores.get(proceso.split()[0], RESET_COLOR)
            barra_final += f"{color}{proceso.split()[0]}{RESET_COLOR} "
    print(barra_final)

def round_robin(procesos, quantum):
    tiempo_actual = 0
    cola = []
    resultados = []
    log_procesador = []

    # Mientras haya procesos por ejecutar o en la cola
    while procesos or cola:
        # Añadimos procesos que inician en el tiempo actual
        while procesos and procesos[0].inicio <= tiempo_actual:
            cola.append(procesos.pop(0))

        if cola:
            proceso = cola.pop(0)
            imprimir_barra(tiempo_actual, proceso.id, cola)
            log_procesador.append(f"P{proceso.id} ({tiempo_actual})")
            sleep(0.5)  # Simulación visual con pausa

            # Actualizamos el tiempo de primer uso si es la primera vez que se ejecuta
            if proceso.tiempo_primer_uso is None:
                proceso.tiempo_primer_uso = tiempo_actual

            tiempo_ejecucion = min(proceso.tiempo_restante, quantum)
            proceso.tiempo_restante -= tiempo_ejecucion
            tiempo_actual += tiempo_ejecucion

            # Añadimos procesos que llegaron mientras este proceso ejecutaba
            while procesos and procesos[0].inicio <= tiempo_actual:
                cola.append(procesos.pop(0))

            # Si el proceso no ha terminado, regresa a la cola
            if proceso.tiempo_restante > 0:
                cola.append(proceso)
            else:
                proceso.tiempo_final = tiempo_actual
                proceso.tiempo_espera = proceso.tiempo_final - proceso.inicio - proceso.duracion
                proceso.tiempo_servicio = proceso.tiempo_final - proceso.tiempo_primer_uso
                resultados.append(proceso)
        else:
            # Si no hay procesos listos, avanzamos en el tiempo
            imprimir_barra(tiempo_actual, "No hay nada", cola)
            log_procesador.append("No hay nada")
            sleep(0.5)  # Simulación visual con pausa
            tiempo_actual += 1

    return resultados, log_procesador

def mostrar_resultados(resultados):
    print("\nResultados:")
    print(f"{'Proceso':<10}{'Espera':<10}{'Tiempo Final':<15}{'Duración Prevista':<20}{'Tiempo Serv.':<15}{'Índice Serv.':<15}")
    for proceso in resultados:
        indice_servicio = proceso.duracion / proceso.tiempo_servicio
        print(f"P{proceso.id:<9} {proceso.tiempo_espera:<9} {proceso.tiempo_final:<14} {proceso.duracion:<19} {proceso.tiempo_servicio:<14} {indice_servicio:<14.2f}")

def main():
    print("Simulación del Algoritmo Round-Robin")
    n = int(input("Ingrese el número de procesos: "))
    procesos = []

    for i in range(n):
        inicio = int(input(f"Ingrese el instante de inicio del proceso P{i+1}: "))
        duracion = int(input(f"Ingrese el tiempo de duración del proceso P{i+1}: "))
        procesos.append(Proceso(i + 1, inicio, duracion))

    quantum = int(input("Ingrese el slice del procesador (quantum): "))

    # Ordenamos los procesos por instante de inicio
    procesos.sort(key=lambda p: p.inicio)

    # Ejecutamos el algoritmo Round-Robin
    resultados, log_procesador = round_robin(procesos, quantum)

    # Mostramos la barra final de ejecución
    imprimir_barra_final(log_procesador)

    # Mostramos los resultados finales
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()
