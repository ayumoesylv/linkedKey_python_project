class Queue:
    def __init__(self):
        self.elements = []

    def en_queue(self, x):
        self.elements.append(x)

    def de_queue(self):
        if self.size() != 0:
            self.elements.pop(0)
        else:
            pass

    def peek(self):
        if self.size() != 0:
            return self.elements[0]
        return None

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def clear(self):
        for i in range(0, self.size()):
            self.elements.pop(i)

    def size(self):
        return len(self.elements)

    def __str__(self):
        stri = ""
        for i in self.elements:
            c = str(i)
            stri = stri + c
        return stri


