import heapq
import time

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, inicio, fin, peso):
        if inicio in self.vertices and fin in self.vertices:
            self.vertices[inicio][fin] = peso

def dijkstra(grafo, inicio, final):
    distancias = {vertice: float('inf') for vertice in grafo.vertices}
    distancias[inicio] = 0
    pq = [(0, inicio)]

    while pq:
        distancia_actual, vertice_actual = heapq.heappop(pq)

        if vertice_actual == final:
            return distancias[final]

        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in grafo.vertices[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(pq, (distancia, vecino))

    return float('inf')

def generar_ejemplos():
    ejemplos = [
        (("A", "C"), {"A": {"B": 3, "C": 10}, "B": {"C": 6}}),
        (("A", "E"), {"A": {"B": 5, "C": 6}, "B": {"C": 2}, "C": {"D": 8, "E": 9}, "D": {"E": 4}}),
        (("A", "E"), {"A": {"B": 3, "C": 5}, "B": {"D": 1}, "C": {"E": 2}, "D": {"E": 2}}),
        (("A", "D"), {"A": {"B": 2}, "B": {"D": 3, "C": 2}, "C": {"D": 2}}),
        (("A", "F"), {"A": {"B": 3, "C": 4}, "B": {"C": 4, "E": 1}, "C": {"D": 2}, "D": {"E": 5, "F": 2}, "E": {"F": 6}})
    ]

    for i, (inicio_fin, conexiones) in enumerate(ejemplos):
        inicio, final = inicio_fin
        grafo = Grafo()

        for nodo, conexiones_nodo in conexiones.items():
            grafo.agregar_vertice(nodo)
            for vecino, peso in conexiones_nodo.items():
                grafo.agregar_vertice(vecino)
                grafo.agregar_arista(nodo, vecino, peso)

        start_time = time.time()
        distancia_minima = dijkstra(grafo, inicio, final)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Ejemplo {i + 1}:")
        print(f"Distancia mínima desde el nodo '{inicio}' hasta el nodo '{final}': {distancia_minima}")
        print(f"Tiempo de ejecución: {execution_time} segundos")
        print("\n")

generar_ejemplos()
