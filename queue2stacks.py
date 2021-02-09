# Imported to test.py, sequence steps listed below

class Queue2Stacks:
    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # FILL OUT CODE HERE
        self.stack1.append(element)
        pass
    
    def dequeue(self):
        # FILL OUT CODE HERE
        if not self.stack2: # [0, 1, 2, 3, 4] | []
            while self.stack1: # [4, 3, 2, 1] | [4, 3, 2, 1]
                # Add the elements to stack2 to the reverse order when called
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
        pass
