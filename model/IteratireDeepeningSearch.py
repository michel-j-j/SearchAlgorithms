from data_structure.LIFOQueue import LIFOQueue
from data_structure.Node import Node

class IterativeDeepeningSearch:

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        for depth in range(0, 10000):
            result = self.depth_limited_search(depth)
            if result != 'cutoff':
                return result
        return None

    def depth_limited_search(self, l):
        node = Node(self.problem.initial)
        frontier = LIFOQueue()
        frontier.add(node)
        result = None
        while not frontier.is_empty():
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                return node
            else:
                print(node.state, node.path_cost)
            if self.depth(node) > l:
                result = 'cutoff'
            elif not self.is_cycle(node):
                for child in self.expand(node):
                    frontier.add(child)
        return result

    def expand(self, node):
        s = node.state
        for action in self.problem.get_actions(s):
            s_prime = self.problem.result(s, action)
            cost = node.path_cost + self.problem.action_cost(s, action, s_prime)
            yield Node(s_prime, node, action, cost)

    def depth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    def is_cycle(self, node):
        state = node.state
        while node:
            node = node.parent
            if node and node.state == state:
                return True
        return False
    
    def path(self, node):
        path_back = []
        while node:
            path_back.append(node)
            node = node.parent
        return path_back[::-1]