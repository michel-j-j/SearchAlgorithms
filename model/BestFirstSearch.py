from model.data_structure.Node import Node
from model.data_structure.PriorityQueue import PriorityQueue

class BestFirstSearch:
    def __init__(self, problem, f):
        self.problem = problem
        self.f=f
    def search (self):
        node = Node(self.problem.initial) # node-NODE (STATE=problem. INITIAL)
        frontier = PriorityQueue(self.f) # frontier a priority queue ordered by f, with node as an element
        frontier.add(node) # add node to frontier
        reached = {self.problem.initial: node} 
        while not frontier.is_empty():
            node = frontier.pop() # node-POP (frontier)
            if self.problem.goal_test(node.state):
                return node
            else:
                print (node.state, node.path_cost)
            for child in self.expand (node):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s]= child
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