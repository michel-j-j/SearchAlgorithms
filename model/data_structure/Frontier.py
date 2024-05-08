class Frontier:
    def __init__(self):
          self.elements = []
    def is_empty(self):
        return len(self.elements) == 0
    def pop(self):
         return self.elements.pop(0)
    def top(self):
         return self.elements[0]
    def add(self, node):
         pass