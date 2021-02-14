#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None
#
#                r
#              /   \
#            a       b
#          /   \   /   \
#         c     n n     n
#       /   \  
#      d     n
# How to keep the breadth and depth of the tree balanced?

    def add(self, new_node, current=None):
        if not current:
            current = self.root
        

        if not current.left:
            current.left = new_node
        elif not current.right:
            current.right = new_node

        return self.add(new_node, current=current.left)