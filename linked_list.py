#!/usr/bin/env python3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# 1 -> 2 -> 3 -> 4 -> 5
# 1 .. 2 .. 3 .. 4 .. 5
class LinkedList:

# adding a node

    def __init__(self):
        self.head = None
    
    def add(self, data, prev_node=None, position=None):

        new_node = Node(data)


        if not self.head:
            self.head = new_node
            return True


        if prev_node:
            # set reference for current state, make variable, then assign
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            return True
        
        
        if position:
            last = self.find_index(index=position)
            if last == self.head:
                last.next = self.head
                self.head = last
                return True
            return self.add(data, prev_node=last)
        
        last = self.find_index()
        last.next = new_node
        return True


# Removing a node
 
    def remove(self, data):

# Store the head node

        temp = self.head

        if temp is not None:
            if (temp.data == data):
                self.head = temp.next
                return True
            
            while (temp is not None):
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next

            # What happens if what we are trying to delete is not in the list??
            if (temp == None):
                return "Data was not found, nothing was removed."

            prev.next = temp.next

            return True
        return "There is no data at the head of the list, nothing was removed."
        
  
    def find_index(self, index=None):
        last = self.head
        counter = 0
        while (last.next):
            last = last.next
            
            if counter == index:
                break
            counter += 1
        return last

