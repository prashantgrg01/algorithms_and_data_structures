"""
-------------------------
Created on Jul 20, 2018

@author: Prashant Gurung
-------------------------

Queue Implementation using Linked List

Methods:
is_empty() => O(1) => returns whether the queue is empty or not
enqueue(item) => O(1) => inserts a new item at the end of the queue
dequeue() => O(1) => removes an item at the start of the queue
peek_front() => O(1) => returns the item at the start of the queue without removing it
peek_back() => O(1) => returns the item at the end of the queue without removing it

"""

# Node definition for Queue
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the next node
        self.next = None
    
    def __str__(self):
        return "< " + str(self.data) + " >"

# Class definition for Queue
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
    
    def is_empty(self):
        return self.head == None
    
    def enqueue(self, item):
        # create new node with the item
        node = Node(item)
        # check if the queue is empty or not
        if self.is_empty():
            # make the new node our head node as well as tail node
            self.head = node
            self.tail = node
        else:
            # make the current tail node point to the new node
            self.tail.next = node
            # make the new node our new tail node
            self.tail = node
        # increase the size of our queue
        self.__size += 1
    
    def dequeue(self):
        # check if the queue is empty
        if self.is_empty():
            # if so there are no items to remove from the queue
            print("Queue empty!")
        else:
            # temporarily store the current head node
            temp = self.head
            # update the head node to point to the next node
            self.head = self.head.next
            # if the current head node happens to be None then the queue is empty
            if self.head is None:
                # so also make the tail node None
                self.tail = None
            # delete the previous head node
            del temp
            # decrease the size of our queue
            self.__size -= 1

    def peek_front(self):
        if self.is_empty():
            print("Queue empty!")
        else:
            # return the first item in the queue
            return self.head.data

    def peek_back(self):
        if self.is_empty():
            print("Queue empty!")
        else:
            # return the last item in the queue
            return self.tail.data

    def __len__(self):
        return self.__size

    def __str__(self):
        # check if the queue is empty
        if self.is_empty():
            return "Queue empty!"
        else:
            # initialize result to empty string
            res = ""
            # start from head node
            current = self.head
            # loop until we reach the end of our queue
            while current is not None:
                # add each node's data to our result
                res += str(current.data) + " => "
                # move on to the next node
                current = current.next
            # return the result by removing the last 4 characters i.e. " => "
            return res[:-4]

# testing our queue
def test_queue():
    # create new queue of fruits
    fruits = Queue()

    # test empty queue
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))
    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())

    # inserting items to our queue
    fruits.enqueue("apple")
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))
    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())
    fruits.enqueue("orange")
    fruits.enqueue("mango")
    fruits.enqueue("papaya")
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))

    # peeking items in our queue
    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())

    # removing item from our queue
    fruits.dequeue()
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))
    fruits.dequeue()
    fruits.dequeue()
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))
    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())

    # making the queue empty
    fruits.dequeue()
    print(fruits)
    print("Queue empty?", fruits.is_empty())
    print("Items in queue:", len(fruits))
    print("First item:", fruits.peek_front())
    print("Last item:", fruits.peek_back())


if __name__ == "__main__":
    test_queue()
    

    

    