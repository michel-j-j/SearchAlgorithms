def depth_limited_search(graph, start, goal, limit):
    def recursive_dls(node, goal, limit, path):
        if node == goal:
            return 'Encontrado', path
        if limit <= 0:
            return 'Limite alcançado', None
        for child in graph.get(node, []):
            result, child_path = recursive_dls(child, goal, limit - 1, path + [child])
            if result == 'Encontrado':
                return 'Encontrado', child_path
        return 'Limite alcançado', None

    return recursive_dls(start, goal, limit, [start])

# Função main que executa o DLS
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
    start_node = 'A'
    goal_node = 'G'
    depth_limit = 4

    # Executa o DLS
    print("Busca com Profundidade Limitada (DLS):")
    result, path = depth_limited_search(graph, start_node, goal_node, depth_limit)
    if result == 'Encontrado':
        print(f"Caminho encontrado: {' -> '.join(path)}")
    else:
        print(result)

# Chama a função main
if __name__ == "__main__":
    main()
