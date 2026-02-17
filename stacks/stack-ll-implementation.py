class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, val):
        newNode = Node(val)
        newNode.next = self.top
        self.top = newNode
        self.height += 1

    def pop(self):
        if self.top == None:
            return
        out = self.top
        self.top = self.top.next
        self.height -= 1
        return out.value
        
    def peek(self):
        if self.top == None:
            return
        return self.top.value