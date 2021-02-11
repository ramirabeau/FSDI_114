#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""LinkedList Test Parameters """

from linked_list import LinkedList
# Received error on line 39 in linked_list.py; will not import LinkedList 

def test_add_beginning():
    llist = LinkedList()
    llist.add("A")
    assert llist.head.data == "A"

def test_add_end():
    llist = LinkedList()
    for i in range(10):
        llist.add(i)
    llist.add(11)
    last = llist.find_index()
    assert last.data == 11

def test_add_position():
    llist = LinkedList()
    for i in range(10):
        llist.add(i)
    llist.add(100, position=5)
    vi_node = llist.find_index(index=6)
    assert vi_node.data == 100

def test_add_head ():
    llist = LinkedList()
    llist.add("Z")
    assert llist.head.data == "Z"