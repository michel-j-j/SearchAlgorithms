from model.data_structure.Frontier import Frontier

class FIFOQueue(Frontier):

    def __init__(self):
        super().__init__()

    def add(self, node):
        self.elements.append(node)
