"""
-------------------------
Created on Jul 10, 2018

@author: Prashant Gurung
-------------------------

Singly Linked List Implementation using Head and Tail pointers

Methods:
is_empty() => O(1) => checks whether the list is empty or not
push_front(item) => O(1) => inserts a new item at the beginning of the list
pop_front() => O(1) => removes the first item from the list
peek_front() => O(1) => returns the first item of the list without removing it
push_back(item) => O(1) => inserts a new item at the end of the list
pop_back() => O(n) => removes the last item from the list
peek_back() => O(1) => returns the last item of the list without removing it
insert_before(target, item) => O(n) => inserts a new item before the target item in the list
insert_after(target, item) => O(n) => inserts a new item after the target item in the list
remove(item) => O(n) => removes an item from the list if it exists
search(item) => O(n) => searches for an item in the list

"""

# Node definition for Singly Linked List
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the next node
        self.next = None

    def __str__(self):
        return "< " + str(self.data) + " >" 

# Class definition for Singly Linked List
class SinglyLinkedList(object):
    def __init__(self):
        # initialize head and tail pointers to None and list size to 0
        self.head = None
        self.tail = None
        self.__size = 0

    def is_empty(self):
        return self.head == None

    def push_front(self, item):
        # create a new node with the item
        node = Node(item)
        # make the new node point to the current head node
        node.next = self.head
        # make the new node our head node
        self.head = node
        # if the tail node is None i.e. its an empty list
        if self.tail is None:
            # also make the new node our tail node
            self.tail = node
        # increase the size of our list
        self.__size += 1
    
    def pop_front(self):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # store current head node in temp
            temp = self.head
            # update the head node to the next node
            self.head = self.head.next
            # if the head node is None i.e. the list is empty
            if self.head is None:
                # also make the tail node None
                self.tail = None
            # delete the previous head node
            del temp
            # decrease the size of our list
            self.__size -= 1

    def peek_front(self):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # return the data of our current head node
            return self.head.data
    
    def push_back(self, item):
        # create a new node with the item
        node = Node(item)
        # check if the list is empty
        if self.is_empty():
            # make the new node our head node as well as the tail node
            self.head = node
            self.tail = node
        else:
            # make the tail node point to our new node
            self.tail.next = node
            # make the new node our tail node
            self.tail = node
        # increase the size of our list
        self.__size += 1
    
    def pop_back(self):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # store current tail node in temp
            temp = self.tail
            # if the head node also happens to be the tail node i.e. there is only one item in the list
            if self.head == self.tail:
                # update both the head node and the tail node to None
                self.head = None
                self.tail = None
            else:
                # start from the head node
                current = self.head
                # loop until we reach a node that points to our tail node
                while current.next != self.tail:
                    current = current.next
                # make the current node point to None
                current.next = None
                # make the current node our tail node
                self.tail = current
            # delete the previous tail node
            del temp
            # decrease the size of our list
            self.__size -= 1

    def peek_back(self):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # return the data of our current tail node
            return self.tail.data

    def insert_before(self, target, item):
        # create a new node with the item
        node = Node(item)
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        elif self.head.data == target:
            # if the target item is our head node, make the new node point to the current head node
            node.next = self.head
            # make the new node our head node
            self.head = node
            # increase the size of our list
            self.__size += 1
        else:
            # start from head node
            current = self.head
            # loop until the target item is found or we reach the end of the list
            while current.data != target and current.next is not None:
                # keep track of previous node
                prev = current
                current = current.next
            # if the target item is found
            if current.data == target:
                # make the new node point to the target node
                node.next = current
                # make the previous node point to the new node
                prev.next = node
                # increase the size of our list
                self.__size += 1
            else:
                # if the target item is not found then say so
                print("Target item doesn't exist in the list!")

    def insert_after(self, target, item):
        # create a new node with the item
        node = Node(item)
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        else:
            # start from head node
            current = self.head
            # loop until the target item is found or we reach the end of the list
            while current.data != target and current.next is not None:
                current = current.next
            # if the target item is found
            if current.data == target:
                # make the new node point to the next node pointed by the target node
                node.next = current.next
                # make the target node point to the new node
                current.next = node
                # if the target node happens to be the tail node
                if current == self.tail:
                    # make the new node our tail node
                    self.tail = node
                # increase the size of our list
                self.__size += 1
            else:
                # if the target item is not found then say so
                print("Target item doesn't exist in the list!")

    def remove(self, item):
        # check if the list is empty
        if self.is_empty():
            print("Linked list empty!")
        elif self.head.data == item:
            # if the item is in the head node then store head node in temp
            temp = self.head
            # update the head node to the next node
            self.head = self.head.next
            # if the head node is None i.e. the list is empty
            if self.head is None:
                # also make the tail node None
                self.tail = None
            # delete the previous head node
            del temp
            # decrease the size of our list
            self.__size -= 1
        else:
            # start from head node
            current = self.head
            # loop until the item to be removed is found or we reach the end of the list
            while current.data != item and current.next is not None:
                # keep track of previous node
                prev = current
                current = current.next
            # if the item to be removed is found
            if current.data == item:
                # make previous node point to the next node pointed by the current node
                prev.next = current.next
                # if the current node happens to be the tail node
                if current == self.tail:
                    # make the previous node our tail node
                    self.tail = prev
                # delete the current node
                del current
                # decrease the size of our list
                self.__size -= 1
            else:
                # if the item to be removed is not in the list say so
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
            # loop until we reach the end of our singly linked list
            while current is not None:
                # add each node's data to our result
                res += "{ " + str(current.data) + " } => "
                # move on to the next node
                current = current.next
            # return the result by removing the last 4 characters i.e. " => "
            return res[:-4]

# testing our singly linked list
def test_ssl():
    fruits = SinglyLinkedList()
    
    print(fruits.is_empty())
    print("Number of items:", len(fruits))

    fruits.push_front("mango")
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.push_back("guava")
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.insert_before("mango", "apple")
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.insert_after("mango", "orange")
    print(fruits)
    print("Number of items:", len(fruits))

    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())
    print("Is orange in the list?", fruits.search("orange"))
    print("Is strawberry in the list?", fruits.search("strawberry"))

    fruits.pop_front()
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.pop_back()
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.remove("orange")
    print(fruits)
    print("Number of items:", len(fruits))

    fruits.remove("mango")
    print(fruits)
    print("Number of items:", len(fruits))

if __name__ == "__main__":
    test_ssl()