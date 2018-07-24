"""
-------------------------
Created on Jul 19, 2018

@author: Prashant Gurung
-------------------------

Stack Implementation using Linked List

Methods:
is_empty() => O(1) => returns whether the stack is empty or not
push(item) => O(1) => inserts a new item on top of the stack
pop() => O(1) => removes the top item from the stack
peek() => O(1) => returns the top item from the stack without removing it

"""

# Node definition for Stack
class Node(object):
    def __init__(self, data):
        # stores the data item for current node
        self.data = data
        # pointer to the next node
        self.next = None

    def __str__(self):
        return "< " + str(self.data) + " >"

# Class definition for Stack
class Stack(object):
    def __init__(self):
        self.head = None
        self.__size = 0
    
    def is_empty(self):
        return self.head == None

    def push(self, item):
        # create new node with the item
        node = Node(item)
        # check if the stack is empty
        if self.is_empty():
            # make new node the first node in our stack
            self.head = node
        else:
            # make new node point to the current top node of the stack
            node.next = self.head
            # make the new node our new top node
            self.head = node
        # increase the size of our stack
        self.__size += 1
    
    def pop(self):
        # check if the stack is empty
        if self.is_empty():
            # if so there are no items to pop off from the stack
            print("Stack empty!")
        else:
            # temporarily store the current top node of the stack
            temp = self.head
            # store the item to return
            res = self.head.data
            # make the next node pointed by the head our new top node of the stack
            self.head = self.head.next
            # delete the previous top node of the stack
            del temp
            # decrease the size of our stack
            self.__size -= 1
            # return the popped item
            return res
    
    def peek(self):
        # check if the stack is empty
        if self.is_empty():
            # if so there are no items to peek on the stack
            print("Stack empty!")
        else:
            # return item from the current top node of the stack
            return self.head.data

    def __len__(self):
        return self.__size
    
    def __str__(self):
        # check if the stack is empty
        if self.is_empty():
            return "Stack empty!"
        else:
            # initialize result to empty string
            res = ""
            # start from top node
            current = self.head
            # loop until we reach the bottom node of our stack
            while current is not None:
                # add each node's data to our result
                res += "{ " + str(current.data) + " }\n"
                # move one node down below the current node
                current = current.next
            # return the result removing the last new line
            return res[:-1]


# testing our stack
def test_stack():
    # create new stack
    fruits = Stack()
    # testing empty stack
    print("Is stack empty?", fruits.is_empty())
    print("Items on stack:", len(fruits))
    popped_fruit = fruits.pop()
    print("Popped fruit:", popped_fruit)
    peeked_fruit = fruits.peek()
    print("Peeked fruit:", peeked_fruit)
    print(fruits)

    # pushing items onto stack
    fruits.push("apple")
    print(fruits)
    print("Is stack empty?", fruits.is_empty())
    print("Items on stack:", len(fruits))
    fruits.push("orange")
    print(fruits)
    print("Items on stack:", len(fruits))
    fruits.push("guava")
    fruits.push("mango")
    print(fruits)
    print("Items on stack:", len(fruits))

    # peeking item in non-empty stack
    fruit = fruits.peek()
    print("Top fruit:", fruit)

    # popping items from stack
    fruit = fruits.pop()
    print("Popped fruit:", fruit)
    print(fruits)
    print("Items on stack:", len(fruits))
    fruit = fruits.pop()
    fruit = fruits.pop()
    print("Popped fruit:", fruit)
    print(fruits)
    print("Items on stack:", len(fruits))
    fruit = fruits.pop()
    print("Popped fruit:", fruit)
    print(fruits)
    print("Items on stack:", len(fruits))


if __name__ == "__main__":
    test_stack()


            

