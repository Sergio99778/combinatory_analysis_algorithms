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

        # Encuentra los arcos de corte
        visited = [False] * self.ROW
        self.bfs(source, visited)

        # Configuración final de la matriz después de calcular el flujo máximo
        final_configuration = self.graph

        return max_flow, visited, final_configuration

    # Implementación de BFS para encontrar arcos de corte
    def bfs(self, s, visited):
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if val > 0 and not visited[ind]:
                    queue.append(ind)
                    visited[ind] = True


# Ejemplo de uso del algoritmo de flujo máximo
# 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 12, 15, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 15, 6, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 4, 6, 0, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 
# 0, 0, 0, 0, 5, 0, 0, 0, 15, 0, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 
# 0, 0, 0, 0, 0, 0, 3, 0, 0, 15, 0, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
graph = [[0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 15, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 15, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 0, 15, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

grafo_flujo = GrafoDeFlujo(graph)

fuente = 0
sumidero = 10

flujo_max, arcos_de_corte, configuracion_final = grafo_flujo.flujo_maximo(fuente, sumidero)

print("El flujo máximo es %d unidades" % flujo_max)
print("Los arcos de corte son:", arcos_de_corte)
print("La configuración final de la matriz es:", configuracion_final)
