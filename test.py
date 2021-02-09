#!/usr/bin/env python3 

from queue2stacks import Queue2Stacks


def test():
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())


# Place this if statement in every code
if __name__ == "__main__":
    test()