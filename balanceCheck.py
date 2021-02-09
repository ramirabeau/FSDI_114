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

# receive input to test

#compare to modulus of the number (n)
# if the string were reversed, you should get the same result. Insert Reverse function

def balance_check(s):
    if len(s)%2 !=0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


# half the string and assign the two halves a variable half1 and half2
# run the reverse function on the half2
# compare, half1 should = half2

    
""" class Balance_Check:

    def reverse(s):
        my_check = Check()
        for char in s:
            my_check.push(char)
        s = ""

        while not my_check.is_empty():
            s += my_check.pop()
        return s
 """