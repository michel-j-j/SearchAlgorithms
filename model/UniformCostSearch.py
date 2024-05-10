import heapq
from queue import PriorityQueue

# Algoritmo de Dijkstra
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Busca de Custo Uniforme
def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    
    while not queue.empty():
        cost, node, path = queue.get()
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return cost, path
        
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                queue.put((cost + weight, neighbor, path + [neighbor]))
    
    return float("infinity"), []

# Função main 
def main():
    graph = {
        'A': {'B': 2, 'D': 6},
        'B': {'A': 2, 'C': 5},
        'C': {'B': 5, 'D':8, 'F': 10, 'E': 15},
        'D': {'A': 6, 'C': 8},
        'E': {'C': 15, 'F': 6, 'G': 6},
        'F': {'C':10, 'E':6, 'G':2},
        'G': {'E':6, 'F':2}
    }
    start = 'A'
    goal = 'G'

    # Executa o Algoritmo de Dijkstra
    print("Algoritmo de Dijkstra:")
    distances = dijkstra(graph, start)
    for vertex in distances:
        print(f"Distância do vértice {start} até {vertex} é {distances[vertex]}")
    
    # Executa a Busca de Custo Uniforme
    print("\nBusca de Custo Uniforme:")
    cost, path = uniform_cost_search(graph, start, goal)
    print(f"Custo do caminho de {start} até {goal} é {cost}")
    print(f"Caminho: {' -> '.join(path)}")

# Chama a função main
if __name__ == "__main__":
    main()
