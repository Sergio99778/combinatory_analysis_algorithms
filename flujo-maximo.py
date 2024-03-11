class GrafoDeFlujo:
    def __init__(self, graph):
        self.graph = graph  # Guarda el grafo de flujo residual
        self.ROW = len(graph)

    # Implementación del algoritmo de búsqueda de caminos usando DFS
    def DFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        stack = [s]
        visited[s] = True

        while stack:
            u = stack.pop()

            for ind, val in enumerate(self.graph[u]):
                print(visited)
                print("u: ", u, " ind: ", ind, " val: ", val)
                if visited[ind] == False and val > 0:
                    stack.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Implementación del algoritmo de flujo máximo utilizando Ford-Fulkerson
    def flujo_maximo(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.DFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            # Encuentra el flujo máximo del camino encontrado
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Agrega el flujo del camino encontrado al flujo máximo total
            max_flow += path_flow

            # Actualiza las capacidades residuales de los arcos y sus arcos inversos
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Ejemplo de uso del algoritmo de flujo máximo
graph = [[0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 10, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 0, 15, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for row in graph:
    print(len(row))
         

grafo_flujo = GrafoDeFlujo(graph)

fuente = 0
sumidero = 10

print("El flujo máximo es %d unidades" % grafo_flujo.flujo_maximo(fuente, sumidero))
