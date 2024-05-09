from model.data_structure.PriorityQueue import PriorityQueue
from model.data_structure.Node import Node

class BidirectionalBestFirstSearch:
    def __init__(self, problemF, fF, problemB, fB):
        self.problemF = problemF
        self.fF = fF
        self.problemB = problemB
        self.fB = fB
    def search(self):
        nodeF = Node(self.problemF.initial)
        nodeB = Node(self.problemB.initial)
        frontierF = PriorityQueue(self.fF)
        frontierB = PriorityQueue(self.fB)
        frontierF.add(nodeF)
        frontierB.add(nodeB)
        reachedF = {self.problemF.initial: nodeF}
        reachedB = {self.problemB.initial: nodeB}
        solution = None
        while not self.terminated(solution, frontierF, frontierB):
            if self.fF(frontierF.top()) < self.fB(frontierB.top()):
                solution = self.proceed('F', frontierF, reachedF, reachedB, solution)
            else:
                solution = self.proceed('B', frontierB, reachedB, reachedF, solution)
        return solution
    def proceed(self, direction, frontier, reached, reached2, solution):
        node = frontier.pop()
        for child in self.expand(node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
                if s in reached2:
                    solution2 = self.join_nodes(direction, child, reached2[s])
                    if solution is None or solution2[0].path_cost < solution[0].path_cost:
                        solution = solution2

        return solution
    def join_nodes(self, direction, node1, node2):
        if direction == 'F':
            return node1, node2
        else:
            return node2, node1
    def expand(self, node):
        s = node.state
        for action in self.problemF.get_actions(s):
            s_prime = self.problemF.result(s, action)
            cost = node.path_cost + self.problemF.action_cost(s, action, s_prime)
            yield Node(s_prime, node, action, cost)
    def terminated(self, solution, frontierF, frontierB):
        return solution is not None or frontierF.is_empty() or frontierB.is_empty()
    def path(self, node):
        path_back = []
        while node:
            path_back.append(node)
            node = node.parent
        return path_back[::-1]