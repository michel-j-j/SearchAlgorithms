from model.data_structure.Frontier import Frontier

class LIFOQueue(Frontier):
        
        def __init__(self):
            super().__init__()
        
        def add(self, node):
            '''
            ADD(node, frontier) inserts node at the beginning of the queue.
            '''
            self.elements.insert(0, node)