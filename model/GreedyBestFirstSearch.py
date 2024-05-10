import heapq

def greedy_best_first_search(graph, start, goal, heuristics):
    visited = set()
    priority_queue = [(heuristics[start], start)]
    came_from = {start: None}  # Dicionário para rastrear o caminho
    
    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, _ in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))
                came_from[neighbor] = current_node  # Rastreia o caminho
    
    return "Nó objetivo não encontrado."

def reconstruct_path(came_from, start, goal):
    current_node = goal
    path = []
    while current_node != start:  # Reconstrói o caminho de trás para frente
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start)  # Adiciona o nó inicial ao caminho
    path.reverse()  # Inverte o caminho para a ordem correta
    return path

# Exemplo de uso:
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5), ('D', 8), ('F', 10), ('E', 15)],
    'D': [('A', 6), ('C', 8)],
    'E': [('C', 15), ('F', 6), ('G', 6)],
    'F': [('C', 10), ('E', 6), ('G', 2)],
    'G': [('E', 6), ('F', 2)]
}
heuristics = {
    'A': 10, 'B': 8, 'C': 5, 'D': 7,
    'E': 3, 'F': 6, 'G': 0, # Heurística do nó objetivo é sempre 0
}

start_node = 'A'
goal_node = 'G'

path = greedy_best_first_search(graph, start_node, goal_node, heuristics)
if path:
    print(f"Caminho encontrado: {' -> '.join(path)}")
else:
    print("Nó objetivo não encontrado.")
