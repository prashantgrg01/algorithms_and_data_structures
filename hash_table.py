"""
-------------------------
Created on Jul 20, 2018

@author: Prashant Gurung
-------------------------

Hash Table Implementation using Chaining for resolving collisions and DJB2 Hash Algorithm for hashing keys

Methods:
is_empty() => O(1) => returns whether the hash table is empty or not
insert(key, value) => O(1) => inserts (key, value) pair to the hash table
remove(key) => O(1) => removes the given key from the hash table
search(key) => O(1) => searches for the given key in the hash table and returns its value if found else an error

"""

# Node definition for Linked List used in chaining
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the next node
        self.next = None

# Class definition for Linked List used in chaining
class LinkedList(object):
    def __init__(self):
        # initialize head and tail pointers to None and list size to 0
        self.head = None
        self.tail = None
        self.__size = 0
    
    def is_empty(self):
        return self.head == None
        
    def push_back(self, item):
        assert type(item) == tuple, "Item is not a valid tuple of (key, value) pair!"
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
    
    def remove(self, key):
        # check if the list is empty
        if self.is_empty():
            return False
        elif self.head.data[0] == key:
            # if the key is in the head node then store head node in temp
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
            return True
        else:
            # start from head node
            current = self.head
            # loop until the item to be removed is found or we reach the end of the list
            while current.data[0] != key and current.next is not None:
                # keep track of previous node
                prev = current
                current = current.next
            # if the item to be removed is found
            if current.data[0] == key:
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
                return True
            else:
                # if the item to be removed is not in the list say so
                return False

    def search(self, key):
        # check if the list is empty
        if self.is_empty():
            return False
        else:
            # start from head node
            current = self.head
            # loop until the search item is found or we reach the end of the list
            while current.data[0] != key and current.next is not None:
                current = current.next
            # if we found the search item return True else return False
            if current.data[0] == key:
                return True
            else:
                return False
    
    def __len__(self):
        return self.__size

# Class definition for Hash Table
class HashTable(object):
    def __init__(self, size):
        # initialize the size of our hash table
        self.size = size
        # create a hash table with given size
        self.table = []
        for i in range(self.size):
            chained_list = LinkedList()
            self.table.append(chained_list)
        # initialize the count of items in our hash table
        self.count = 0

    # Implementation of Hash Function using DJB2 Hash Algorithm
    def djb2_hash(self, key):
        hash_value = 5381
        for char in key:
            hash_value = hash_value * 33 + ord(char)
        return hash_value

    def is_empty(self):
        return self.count == 0
    
    def insert(self, key, value):
        # generate hash for the given key
        hash_value = self.djb2_hash(key)
        # calculate the valid index to store the (key, value) pair
        index = hash_value % self.size
        # insert the (key, value) pair in the calculated index of our hash table
        self.table[index].push_back((key, value))
        # increase the count of items in our hash table
        self.count += 1

    def remove(self, key):
        # generate hash for the given key
        hash_value = self.djb2_hash(key)
        # calculate the index where the key resides
        index = hash_value % self.size
        # remove the (key, value) pair from our hash table
        success = self.table[index].remove(key)
        # if key is present and removed
        if success:
            # decrease the count of items in our hash table
            self.count -= 1
        else:
            print("Error! Key not found.")
    
    















