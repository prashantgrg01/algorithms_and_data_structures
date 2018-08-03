"""
-------------------------
Created on Jul 31, 2018

@author: Prashant Gurung
-------------------------

Heap Implementation - Binary Max Heap

Methods:
is_empty() => O(1) => returns whether the heap is empty or not
get_max() => O(1) => returns the maximum item of the heap without removing it
pop_max() => O(log n) => returns the maximum item from the heap by removing it
insert(item) => O(log n) => inserts a new item to the heap
update(item, new_item) => O(n log n) => updates an item in the heap

"""

# Class definition for Heap
class Heap(object):
    def __init__(self):
        # array for storing the items of heap
        self.heap = []
    
    def is_empty(self):
        """
        Function to return whether the heap is empty or not
        """
        return self.heap == []

    def get_parent(self, index):
        """
        Function to return the parent of current index
        """
        return (index - 1) // 2
    
    def get_left_child(self, index):
        """
        Function to return the left child of current index
        """
        return 2 * index + 1

    def get_right_child(self, index):
        """
        Function to return the right child of current index
        """
        return 2 * index + 2
    
    def get_greater_child(self, left_child, right_child):
        """
        Function to return the greater child between the left child and the right child
        """
        if self.heap[left_child] > self.heap[right_child]:
            return left_child
        return right_child

    def heapify_up(self, index):
        """
        Function to shift the item in current index up the heap in its correct position
        """
        # if the current item has a parent
        if self.get_parent(index) >= 0:
            # get the parent index of current item
            parent_index = self.get_parent(index)
            # if current item is greater than its parent
            if self.heap[index] > self.heap[parent_index]:
                # swap the current item with its parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # recursively call the same method for its parent
                self.heapify_up(parent_index)

    def heapify_down(self, index):
        """
        Function to shift the item in current index down the heap in its correct position
        """
        # if the current item has two childs
        if self.get_right_child(index) < len(self.heap):
            # get the greater child between the two childs of current item
            greater_child_index = self.get_greater_child(self.get_left_child(index), self.get_right_child(index))
        elif self.get_left_child(index) < len(self.heap):
            # if the current item has only one child, make its left child the greater child
            greater_child_index = self.get_left_child(index)
        else:
            # make the greater child None since it has no childs
            greater_child_index = None
        # if there exists a child and the current item is less than the greater child
        if greater_child_index is not None and self.heap[index] < self.heap[greater_child_index]:
            # swap the current item with the greater child
            self.heap[index], self.heap[greater_child_index] = self.heap[greater_child_index], self.heap[index]
            # recursively call the same method for the greater child
            self.heapify_down(greater_child_index)
    
    def get_max(self):
        """
        Function to return the maximum item of the heap without removing it
        """
        if self.is_empty():
            print("Heap empty!")
        else:
            return self.heap[0]

    def pop_max(self):
        """
        Function to return the maximum item from the heap by removing it
        """
        if self.is_empty():
            print("Heap empty!")
        else:
            # swap the first item with the last item of the heap
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            # remove the last item i.e. the max item from the heap
            max_item = self.heap.pop()
            # if the heap is not empty after removing the max item
            if not self.is_empty():
                # adjust the first item in its correct position down the heap
                self.heapify_down(0)
            # return the max item
            return max_item
    
    def insert(self, item):
        """
        Function to insert a new item in the heap
        """
        # add the new item to the heap i.e. at the end of the heap array
        self.heap.append(item)
        # get the index of the new item i.e. the last item in the heap array
        item_index = len(self.heap) - 1
        # adjust the new item i.e. the last item in its correct position up the heap
        self.heapify_up(item_index)
    
    def update(self, item, new_item):
        """
        Function to update an item in the heap
        """
        if self.is_empty():
            print("Heap empty!")
        else:
            # loop through each item in the heap until we find the item to update
            index = 0
            found = False
            while found == False and index < len(self.heap):
                # if the current item is the item we want to update
                if item == self.heap[index]:
                    # set found to True to signify that the item to update was found
                    found = True
                    # update the item
                    self.heap[index] = new_item
                    # if the current item is greater than its parent
                    if self.heap[index] > self.heap[self.get_parent(index)]:
                        # adjust the current item in its correct position up the heap
                        self.heapify_up(index)
                    else:
                        # adjust the current item in its correct position down the heap
                        self.heapify_down(index)
                # move on to the next index
                index += 1
            # if the item is still not found say so
            if found == False:
                print("Item not found!")
    
    def __str__(self):
        if self.is_empty():
            return "Heap empty!"
        else:
            res = "["
            for item in self.heap:
                res += str(item) + ", "
            return res[:-2] + "]"

# testing our heap
def test_heap():
    # create new heap
    heap = Heap()

    # test empty heap
    print("Is heap empty?", heap.is_empty())
    print("Maximum item of heap:", heap.pop_max())
    print(heap)

    # insert items to heap
    heap.insert(50)
    heap.insert(30)
    heap.insert(70)
    heap.insert(45)
    heap.insert(15)
    print("Is heap empty?", heap.is_empty())
    print(heap)

    # get max item from the heap
    print("Maximum item of heap:", heap.get_max())
    print(heap)

    # remove max item from the heap
    print("Maximum item of heap:", heap.pop_max())
    print(heap)

    # update an item that is present in the heap
    heap.update(15, 60)
    print(heap)

    # update an item that is not present in the heap
    heap.update(20, 40)
    print(heap)

if __name__ == "__main__":
    test_heap()
