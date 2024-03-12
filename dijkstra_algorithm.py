import sys

def dijkstra(graph, start, end):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0
    visited = set()

    while visited != set(graph):
        min_distance = sys.maxsize
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        for neighbor, weight in graph[min_vertex].items():
            distance = distances[min_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.add(min_vertex)

    path = []
    current_vertex = end
    total_weight = 0
    while current_vertex != start:
        path.append(current_vertex)
        next_vertex = min(graph[current_vertex], key=lambda x: distances[x])
        total_weight += graph[current_vertex][next_vertex]
        current_vertex = next_vertex

    path.append(start)
    path.reverse()

    return path, total_weight

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start_vertex = 'A'
end_vertex = 'F'

shortest_path, total_weight = dijkstra(graph, start_vertex, end_vertex)
print(f"El camino más corto desde {start_vertex} hasta {end_vertex} es: {shortest_path}")
print(f"Peso total del camino: {total_weight}")