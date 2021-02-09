class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items) 

# Instructor solution

    def reverse(string):
        my_stack = Stack()
        for char in string:
            my_stack.push(char)
        out = ""

        while not my_stack.is_empty():
            out += my_stack.pop()
        return out