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
        # make the new node point to head node
        newNode.next = self.head
        # check if the list is empty
        if self.is_empty():
            # if so make new node the tail node
            self.tail = newNode
        else:
            # else make the previous pointer of head node point to the new node
            self.head.prev = newNode
        # make the new node our head node
        self.head = newNode
        # increase the size of our list
        self.__size += 1

    def pop_front(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            # temporarily store the current head node
            node = self.head
            # make the next node pointed by head node our new head
            self.head = self.head.next
            # if current head is none then the list is empty
            if self.head is None:
                # so also make the tail none
                self.tail = None
            else:
                # make the previous pointer of current head node point to none
                self.head.prev = None
            # delete the previous head node
            del node
            # decrease the size of our list
            self.__size -= 1
    
    def peek_front(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            # return the current head node
            return self.head

    def push_back(self, newNode):
        assert type(newNode) == Node, "Invalid node passed!"
        # make the previous pointer of new node point to current tail node
        newNode.prev = self.tail
        if self.is_empty():
            # if the list is empty then make new node our head node
            self.head = newNode
        else:
            # make the next pointer of current tail node point to the new node
            self.tail.next = newNode
        # make the new node our tail node
        self.tail = newNode
        # increase the size of our list
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            # temporarily store the current tail node
            node = self.tail
            # make the previous node pointed by current tail node our new tail node
            self.tail = self.tail.prev
            # if the current tail happens to be none then the list is empty
            if self.tail is None:
                # so also make the head none
                self.head = None
            else:
                # make the next pointer of our current tail node point to none
                self.tail.next = None
            # delete the previous tail node
            del node
            # decrease the size of our list
            self.__size -= 1
    
    def peek_back(self):
        if self.is_empty():
            print("Linked list empty!")
        else:
            # return the current tail node
            return self.tail
    
    def insert_before(self, targetNode, newNode):
        """
        Function assumes the following to work:
        - the list is not empty
        - the target node exists in the list
        """
        assert type(targetNode) == Node and type(newNode) == Node, "Invalid node passed!"
        # make the previous pointer of new node point to the previous node pointed by the target node
        newNode.prev = targetNode.prev
        # make the next pointer of new node point to the target node
        newNode.next = targetNode
        # make the previous pointer of target node point to the new node
        targetNode.prev = newNode
        # if the target node happens to be the head node
        if targetNode == self.head:
            # make the new node our head node
            self.head = newNode
        else:
            # make the next pointer of previous node pointed by the new node point to itself
            newNode.prev.next = newNode
        # increase the size of our list
        self.__size += 1

    def insert_after(self, targetNode, newNode):
        """
        Function assumes the following to work:
        - the list is not empty
        - the target node exists in the list
        """
        assert type(targetNode) == Node and type(newNode) == Node, "Invalid node passed!"
        # make the next pointer of new node point to the next node pointed by the target node
        newNode.next = targetNode.next
        # make the previous pointer of new node point to the target node
        newNode.prev = targetNode
        # make the next pointer of target node point to the new node
        targetNode.next = newNode
        # if the target node happens to be the tail node
        if targetNode == self.tail:
            # make the new node our tail node
            self.tail = newNode
        else:
            # make the previous pointer of next node pointed by the new node point to itself
            newNode.next.prev = newNode
        # increase the size of our list
        self.__size += 1

    def remove(self, targetNode):
        assert type(targetNode) == Node, "Invalid node passed!"
        if self.is_empty():
            print("Linked list empty!")
        elif targetNode == self.head:
            # if the target node happens to be the head node, temporarily store the head node 
            temp = self.head
            # make the next node pointed by the head node our new head
            self.head = self.head.next
            # make the previous pointer of current head node point to none
            self.head.prev = None
            # delete the previous head node
            del temp
            # decrease the size of our list
            self.__size -= 1
        else:
            # start from the head node
            current = self.head
            # loop until the target node is found or we reach the end of the list
            while current != targetNode and current.next is not None:
                current = current.next
            # if the target node is found
            if current == targetNode:
                # make the next pointer of current's previous node point to current's next node
                current.prev.next = current.next
                # check if the current node is the tail node
                if current != self.tail:
                    # if so make the previous pointer of current's next node point to current previous node
                    current.next.prev = current.prev
                else:
                    # make the current's previous node our new tail node
                    self.tail = current.prev
                # delete the current node i.e. the target node
                del current
                # decrease the size of our list
                self.__size -= 1
            else:
                # if the target node is not found say so
                print("Target node doesn't exist in the list!")

    def search(self, targetNode):
        assert type(targetNode) == Node, "Invalid node passed!"
        if self.is_empty():
            print("Linked list empty!")
        else:
            # start from the head node
            current = self.head
            # loop until the target node is found or we reach the end of the list
            while current != targetNode and current.next is not None:
                current = current.next
            # if the target node is found return True else return False
            if current == targetNode:
                return True
            else: 
                return False

    def get_node(self, data):
        if self.is_empty():
            print("Linked list empty!")
        else:
            # start from the head node
            current = self.head
            # loop until the node with search data is found or we reach the end of the list
            while current.data != data and current.next is not None:
                current = current.next
            # if the required node with the search data is found
            if current.data == data:
                # return the node
                return current
            else: 
                # return None denoting that the required node is not found
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

# testing our doubly linked list
def test_dll():
    pass

if __name__ == "__main__":
    test_dll()

        

    