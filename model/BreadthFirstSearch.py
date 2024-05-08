from model.data_structure.Node import Node
from model.data_structure.FIFOQueue import FIFOQueue

class BreadthFirstSearch: 

    def __init__(self, problem):
         self.problem = problem

    def search(self):
        node = Node(self.problem.initial)
        if self.problem.goal_test(node.state):
            return node
        else:
            print(node.state, node.path_cost) 
        frontier= FIFOQueue()
        frontier.add(node)
        reached = [self.problem. initial] # reached-[problem. INITIAL} (como uma lista) while not frontier.is_empty():
        while not frontier.is_empty():
            node = frontier.pop()
            for child in self.expand (node):
                s = child.state
                if self.problem.goal_test(s):
                    return child
                else:
                 print(child.state, child.path_cost)
                if s not in reached:
                 reached.append(s)
                 frontier.add(child)
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