"""
-------------------------
Created on Jul 13, 2018

@author: Prashant Gurung
-------------------------

Doubly Linked List Implementation using Head and Tail pointers

Methods:
is_empty() => O(1) => returns whether the list is empty or not
push_front(newNode) => O(1) => inserts a new node at the beginning of the list
pop_front() => O(1) => removes the first node from the list
peek_front() => O(1) => returns the first node of the list without removing it
push_back(newNode) => O(1) => inserts a new node at the end of the list
pop_back() => O(1) => removes the last node from the list
peek_back() => O(1) => returns the last node of the list without removing it
insert_before(targetNode, newNode) => O(1) => inserts the new node before the target node in the list
insert_after(targetNode, newNode) => O(1) => inserts the new node after the target node in the list
remove(targetNode) => O(n) => removes the target node from the list if it exists
search(targetNode) => O(n) => searches for the target node in the list
get_node(data) => O(n) => searches for the given data item in the list and returns the corresponding node else returns None

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
    
    def is_empty(self):
        return self.head == None

    def push_front(self, newNode):
        assert type(newNode) == Node, "Invalid node passed!"
        newNode.next = self.head
        if self.is_empty():
            self.tail = newNode
        else:
            self.head.prev = newNode
        self.head = newNode

    def pop_front(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            del node
    
    def peek_front(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            return self.head

    def push_back(self, newNode):
        assert type(newNode) == Node, "Invalid node passed!"
        newNode.prev = self.tail
        if self.is_empty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode

    def pop_back(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            node = self.tail
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
            del node
    
    def peek_back(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            return self.tail
    
    # function to insert a new node before a target node
    # assumes that the list is not empty
    # assumes that the target node exists in the list
    def insert_before(self, targetNode, newNode):
        assert type(targetNode) == Node and type(newNode) == Node, "Invalid node passed!"
        newNode.prev = targetNode.prev
        newNode.next = targetNode
        targetNode.prev = newNode
        if targetNode == self.head:
            self.head = newNode
        else:
            newNode.prev.next = newNode

    # function to insert a new node after a target node
    # assumes that the list is not empty
    # assumes that the target node exists in the list
    def insert_after(self, targetNode, newNode):
        assert type(targetNode) == Node and type(newNode) == Node, "Invalid node passed!"
        newNode.next = targetNode.next
        newNode.prev = targetNode
        targetNode.next = newNode
        if targetNode == self.tail:
            self.tail = newNode
        else:
            newNode.next.prev = newNode

    def remove(self, targetNode):
        assert type(targetNode) == Node, "Invalid node passed!"
        if self.is_empty():
            print("Linked list empty!")
        elif targetNode == self.head:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
        else:
            current = self.head
            while current != targetNode and current.next is not None:
                current = current.next
            if current == targetNode:
                current.prev.next = current.next
                if current != self.tail:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                del current
            else:
                print("Target node doesn't exist in the list!")

    def search(self, targetNode):
        assert type(targetNode) == Node, "Invalid node passed!"
        if self.is_empty():
            print("Linked list empty!")
        else:
            current = self.head
            while current != targetNode and current.next is not None:
                current = current.next
            if current == targetNode:
                return True
            else: 
                return False

    def get_node(self, data):
        if self.is_empty():
            print("Linked list empty!")
        else:
            current = self.head
            while current.data != data and current.next is not None:
                current = current.next
            if current.data == data:
                return current
            else: 
                return None

    def __len__(self):
        return self.__size
    
    def __str__(self):
        # check if the list is empty
        if self.is_empty():
            return "Linked list empty!"
        else:
            # initialize result to empty string
            res = ""
            # start from head node
            current = self.head
            # loop until we reach the end of our doubly linked list
            while current is not None:
                # add each node's data to our result
                res += "{ " + str(current.data) + " } => "
                # move on to the next node
                current = current.next
            # return the result by removing the last 4 characters i.e. " => "
            return res[:-4]
    
    def reverse(self):
        # check if the list is empty
        if self.is_empty():
            return "Linked list empty!"
        else:
            # initialize result to empty string
            res = ""
            # start from tail node
            current = self.tail
            # loop until we reach the start of our doubly linked list
            while current is not None:
                # add each node's data to our result
                res += "{ " + str(current.data) + " } => "
                # move on to the previous node
                current = current.prev
            # return the result by removing the last 4 characters i.e. " => "
            return res[:-4]

            



        

    