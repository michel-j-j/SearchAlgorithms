import heapq

def weighted_a_star(graph, start, goal, h, w=1.5):
    open_set = [(h[start] * w, start)]  # Fila de prioridade com o nó inicial e sua heurística ponderada
    came_from = {start: None}  # Para rastrear o caminho
    g_score = {node: float('infinity') for node in graph}  # Custos conhecidos
    g_score[start] = 0  # Custo do início até ele mesmo é zero

    while open_set:
        current_f_score, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor] * w
                heapq.heappush(open_set, (f_score, neighbor))
    
    return "Caminho não encontrado"

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Exemplo de uso:
graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 5},
    'C': {'B': 5, 'D':8, 'F': 10, 'E': 15},
    'D': {'A': 6, 'C': 8},
    'E': {'C': 15, 'F': 6, 'G': 6},
    'F': {'C':10, 'E':6, 'G':2},
    'G': {'E':6, 'F':2}
}
h = {'A': 4, 'B': 3, 'C': 2, 'D': 3, 'E': 1, 'F': 1, 'G': 0}  # Heurística simplificada para o exemplo
start = 'A'
goal = 'G'
weight = 1.5  # Peso aplicado à heurística

path = weighted_a_star(graph, start, goal, h, weight)
if path:
    print(f"Caminho encontrado: {' -> '.join(path)}")
else:
    print("Caminho não encontrado.")
