def ida_star(graph, start, goal, h):
    def search(path, g, threshold):
        node = path[-1]
        f = g + h[node]
        if f > threshold:
            return f, path
        if node == goal:
            return -g, path  # Encontrou o nó objetivo (retorna negativo para indicar sucesso)
        min_cost = float('inf')
        for neighbor, cost in graph[node].items():
            if neighbor not in path:  # Evita ciclos
                new_g = g + cost
                temp, temp_path = search(path + [neighbor], new_g, threshold)
                if temp < 0:  # Encontrou o nó objetivo (retorna negativo para indicar sucesso)
                    return temp, temp_path
                if temp < min_cost:
                    min_cost = temp
                    min_path = temp_path
        return min_cost, path

    threshold = h[start]
    path = [start]
    while True:
        result, path = search(path, 0, threshold)
        if result < 0:
            return path, -result  # Retorna o caminho até o nó objetivo e o custo total
        if result == float('inf'):
            return None, None  # Caminho não encontrado
        threshold = result

# Exemplo de uso:
graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 5},
    'C': {'B': 5, 'D': 8, 'F': 10, 'E': 15},
    'D': {'A': 6, 'C': 8},
    'E': {'C': 15, 'F': 6, 'G': 6},
    'F': {'C': 10, 'E': 6, 'G': 2},
    'G': {'E': 6, 'F': 2}
}
h = {'A': 4, 'B': 3, 'C': 2, 'D': 3, 'E': 1, 'F': 1, 'G': 0}  # Heurística simplificada para o exemplo
start = 'A'
goal = 'G'

path, total_cost = ida_star(graph, start, goal, h)
if path:
    print(f"Caminho encontrado: {' -> '.join(path)}")
    print(f"Custo total do caminho: {total_cost}")
else:
    print("Caminho não encontrado.")
