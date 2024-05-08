from model.data_structure.Frontier import Frontier

class PriorityQueue(Frontier):

    def __init__(self, f):
        super().__init__()
        self.f = f

    def add(self, node):
        self.elements.append(node)
        self.elements = sorted(self.elements, key = self.f)