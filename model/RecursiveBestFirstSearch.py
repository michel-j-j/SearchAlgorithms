def rbfs(graph, start, goal, h, f_limit=float('inf'), path=None, g=0):
    if path is None:
        path = [start]
    if start == goal:
        return path, g  # Retorna o caminho e o custo acumulado

    successors = []
    for neighbor, cost in graph[start].items():
        if neighbor not in path:  # Evita ciclos
            estimated_cost = g + cost + h[neighbor]
            successors.append((neighbor, estimated_cost))

    if not successors:
        return None, float('inf')  # Falha e retorna custo infinito

    while successors:
        # Escolhe o sucessor com o menor custo estimado
        successors.sort(key=lambda x: x[1])
        best = successors[0][0]
        best_f = successors[0][1]

        if best_f > f_limit:
            return None, best_f  # Falha e retorna o melhor custo estimado

        # Alternativa é o segundo melhor custo estimado
        alternative = successors[1][1] if len(successors) > 1 else float('inf')

        result, best_f = rbfs(graph, best, goal, h, min(f_limit, alternative), path + [best], g + graph[start][best])
        successors[0] = (best, best_f)  # Atualiza o custo estimado com o custo retornado

        if result is not None:
            return result, best_f  # Sucesso

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

path, cost = rbfs(graph, start, goal, h)
if path:
    print(f"Caminho encontrado: {' -> '.join(path)}")
    print(f"Custo total do caminho: {cost}")
else:
    print("Caminho não encontrado.")
