import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items)==0
    """It returns true if stack is empty otherwise it returns false"""

    def is_full(self):
        return len(self.items)==self.size
    """It returns true if stack is full otherwise it returns false"""

    def push(self, data):
        if not self.is_full():
            self.items.append(data)
    """It pushes an element to stack if stack is not full"""
        
    def pop(self):
        if not self.is_empty():
            self.items.pop(-1)

    def status(self):
        for elem in self.items:
            print(elem)
    """Display the stack"""

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
