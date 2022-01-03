class Stack:
    def __init__(self):
        self.elements = []

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        top = self.elements[-1]
        self.elements.pop(-1)
        return top

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def clear(self):
        while not self.is_empty():
            self.elements.pop(-1)

    def size(self):
        return len(self.elements)

    def __str__(self):
        for i in self.elements:
            return str(i)