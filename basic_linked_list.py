"""
-------------------------
Created on Jul 10, 2018

@author: Prashant Gurung
-------------------------

Basic Linked List Implementation

Methods:
is_empty() => O(1) => returns whether the list is empty or not
get_size() => O(1) => returns the number of items on the list
insert(item) => O(1) => inserts new item at the beginning of the list
remove(item) => O(n) => removes an item from the list if it is present
search(item) => O(n) => searches for an item in the list

"""

# Node definition for Linked List
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the next node
        self.next = None

# Class definition for Linked List
class LinkedList(object):
    def __init__(self):
        # initialize head pointer to None and list size to 0
        self.head = None
        self.__size = 0

    def is_empty(self):
        return self.head == None

    def get_size(self):
        return self.__size

    def insert(self, item):
        # create a new node with the item
        node = Node(item)
        # make the new node point to the current head node
        node.next = self.head
        # make the new node our head node
        self.head = node
        # increase the size of our list
        self.__size += 1

    def remove(self, item):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        elif self.head.data == item:
            # if the item is in the head node then store head node in temp
            temp = self.head
            # update the head node to point to the next node
            self.head = self.head.next
            # delete the previous head node
            del temp
            # decrease the size of our list
            self.__size -= 1
        else:
            # if the item is not in the head node, start from the head node
            current = self.head
            # loop until the item to be removed is found or we reach the end of the list
            while current.data != item and current.next is not None:
                # keep track of the previous node
                prev = current
                current = current.next
            # if the item to be removed is found
            if current.data == item:
                # make the previous node point to the next node pointed by the current node
                prev.next = current.next
                # delete the current node
                del current
                # decrease the size of our list
                self.__size -= 1
            else:
                # if item to be removed is not found say so
                print("Item doesn't exist in the list!")

    def search(self, item):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # start from head node
            current = self.head
            # loop until the search item is found or we reach the end of the list
            while current.data != item and current.next is not None:
                current = current.next
            # if we found the search item return True else return False
            if current.data == item:
                return True
            else:
                return False
    
    def __str__(self):
        # check if the list is empty
        if self.is_empty():
            return "Linked list empty!"
        else:
            # initialize result to empty string
            res = ""
            # start from head node
            current = self.head
            # loop until we reach the end of our linked list
            while current is not None:
                # add each node's data to our result
                res += " { " + str(current.data) + " } => "
                # move on to the next node
                current = current.next
            # append '!' to our result to denote the end of our result
            res += "!"
            return res

# testing our basic linked list
def test_bll():
    # create our Linked List instance
    bll = LinkedList()

    # testing remove(), search() and get_size() on empty list
    bll.remove("prashant")
    bll.search("suman")
    print("Number of items:", bll.get_size())
    
    # testing insert() on empty list
    bll.insert("prashant")

    # testing insert() on non-empty list
    bll.insert("suman")
    bll.insert("chauhan")
    bll.insert("saurav")
    print(bll)
    print("Number of items:", bll.get_size())

    # testing remove() for middle item on non-empty list
    bll.remove("suman")
    print(bll)
    print("Number of items:", bll.get_size())
    
    # testing search() on non-empty list
    print(bll.search("chauhan"))

    # testing remove() for last item on non-empty list
    bll.remove("prashant")
    print(bll)
    print("Number of items:", bll.get_size())

    # testing remove() for first item on non-empty list
    bll.remove("saurav")
    print(bll)
    print("Number of items:", bll.get_size())

    # testing search() for item not present on the list 
    print(bll.search("saurav"))

    # testing remove() to remove the only item on the list
    bll.remove("chauhan")
    print(bll)
    print("Number of items:", bll.get_size())

if __name__ == "__main__":
    test_bll()

    