import random
import time

def generar_matriz_adyacencia(num_nodos, densidad=0.3):
    matriz = [[float('inf')] * num_nodos for _ in range(num_nodos)]
    for i in range(num_nodos):
        matriz[i][i] = 0
        for j in range(num_nodos):
            if i != j and random.random() < densidad:
                matriz[i][j] = random.randint(1, 20)
    return matriz


def floyd_warshall(matriz):
    n = len(matriz)
    dist = [fila[:] for fila in matriz]  
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


# Prueba
if __name__ == "__main__":
    matriz = generar_matriz_adyacencia(10, 0.4)
    inicio = time.time()
    resultado = floyd_warshall(matriz)
    fin = time.time()
    
    print("Matriz de distancias mínimas:")
    for fila in resultado:
        print(fila)
    print(f"\nTiempo de ejecución: {fin - inicio:.6f} s")
