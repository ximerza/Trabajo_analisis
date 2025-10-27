import heapq
import random
import time

def generar_grafo(num_nodos, densidad=0.3):
    grafo = {i: [] for i in range(num_nodos)}
    for i in range(num_nodos):
        for j in range(num_nodos):
            if i != j and random.random() < densidad:
                peso = random.randint(1, 20)
                grafo[i].append((j, peso))
    return grafo


def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    cola = [(0, origen)]  
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = distancia_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))
    
    return distancias


# Prueba 
if __name__ == "__main__":
    grafo = generar_grafo(10, 0.4)
    inicio = time.time()
    resultado = dijkstra(grafo, 0)
    fin = time.time()
    
    print("Distancias mínimas desde el nodo 0:")
    for nodo, dist in resultado.items():
        print(f"{nodo}: {dist}")
    print(f"\nTiempo de ejecución: {fin - inicio:.6f} s")
