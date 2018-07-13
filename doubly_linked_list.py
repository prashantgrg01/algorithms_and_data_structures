"""
-------------------------
Created on Jul 13, 2018

@author: Prashant Gurung
-------------------------

Doubly Linked List Implementation using Head and Tail pointers

Methods:
is_empty() => O(1) => returns whether the list is empty or not

"""

# Node definition for Doubly Linked List
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the previous node
        self.prev = None
        # pointer to the next node
        self.next = None

    def __str__(self):
        return "< " + str(self.data) + " >" 

# Class definition for Doubly Linked List
class DoublyLinkedList(object):
    def __init__(self):
        # initialize head and tail pointers to None and list size to 0
        self.head = None
        self.tail = None
        self.__size = 0

    