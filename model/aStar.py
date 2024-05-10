import heapq

def a_star(graph, start, goal, h):
    open_set = [(h[start], start)]  # Fila de prioridade com o nó inicial e sua heurística
    came_from = {start: None}  # Para rastrear o caminho
    g_score = {node: float('infinity') for node in graph}  # Custos conhecidos
    g_score[start] = 0  # Custo do início até ele mesmo é zero

    while open_set:
        current_f_score, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    
    return "Caminho não encontrado"

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


graph = {
        'A': {'B': 2, 'D': 6},
        'B': {'A': 2, 'C': 5},
        'C': {'B': 5, 'D':8, 'F': 10, 'E': 15},
        'D': {'A': 6, 'C': 8},
        'E': {'C': 15, 'F': 6, 'G': 6},
        'F': {'C':10, 'E':6, 'G':2},
        'G': {'E':6, 'F':2}
}
h = {'A': 4, 'B': 3, 'C': 2, 'D': 3, 'E': 1, 'F': 1, 'G': 1}  # Heurística 
start = 'A'
goal = 'G'

path = a_star(graph, start, goal, h)
print("Caminho encontrado:", " -> ".join(path))
