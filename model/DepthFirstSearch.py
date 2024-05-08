from model.data_structure.Node import Node

class DepthFirstSearch:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        node = Node(self.problem.initial)
        frontier = [node]  # Utilizamos una lista como una pila para el DFS
        while frontier:
            node = frontier.pop()  # Sacamos el último nodo de la pila
            if self.problem.goal_test(node.state):
                return node
            else:
                print(node.state, node.path_cost)
            for child in self.expand(node):
                frontier.append(child)  # Agregamos los hijos a la pila
        return None

    def expand(self, node):
        s = node.state
        for action in self.problem.get_actions(s):
            s_prime = self.problem.result(s, action)
            cost = node.path_cost + self.problem.action_cost(s, action, s_prime)
            yield Node(s_prime, node, action, cost)

    def path(self, node):
        path_back = []
        while node:
            path_back.append(node)
            node = node.parent
        return path_back[::-1]