"""
-------------------------
Created on Jul 21, 2018

@author: Prashant Gurung
-------------------------

Binary Tree Implementation

Methods:
is_empty() => O(1) => returns whether the binary tree is empty or not
insert(item) => O(log n) => inserts a new item to the binary tree
remove(item) => O(log n) => removes a given item from the binary tree if found
search(item) => O(log n) => searches for a given item to see if it exists in the binary tree or not

"""

# Node definition for Binary Tree
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return "< " + str(self.data) + " >"

# Class definition for Binary Tree
class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.__size = 0

    def is_empty(self):
        return self.root == None

    def insert(self, item):
        # create a new node with the item
        node = Node(item)
        # check if the binary tree is empty
        if self.root is None:
            # if it is then make the new node our root node
            self.root = node
        else:
            # start from the root node
            current = self.root
            # traverse the binary tree until the required parent node is found
            while current is not None:
                parent = current
                if item < current.data:
                    current = current.left
                else:
                    current = current.right
            # if new item is less than the parent node's data
            if item < parent.data:
                # make new node the left child of the parent node
                parent.left = node
            else:
                # make new node the right child of the parent node
                parent.right = node
        # increase the size of our binary tree
        self.__size += 1

    def search(self, item):
        # check if the binary tree is empty
        if self.root is None:
            print("Binary tree empty!")
        else:
            # start from the root
            current = self.root
            # traverse the binary tree until we reach a leaf node or we find the required node
            while current is not None and current.data != item:
                if item < current.data:
                    current = current.left
                else:
                    current = current.right
            # if the required item was not found return False else return True
            if current is None:
                return False
            else:
                return True

    def remove(self, item):
        # check if the binary tree is empty
        if self.root is None:
            print("Binary tree empty!")
        elif self.root.data == item:
            # if the item to remove happens to be the root node then, check if the root has any child
            if self.root.left is None and self.root.right is None:
                # if it has no child then temporarily store the root
                temp = self.root
                # make our binary tree empty
                self.root = None
                # delete the previous root
                del temp
            elif self.root.left is not None and self.root.right is None:
                # if root has only one left child then temporarily store the root
                temp = self.root
                # make the left child of our current root the new root
                self.root = self.root.left
                # delete the previous root
                del temp
            elif self.root.left is None and self.root.right is not None:
                # if root has only one right child then temporarily store the root
                temp = self.root
                # make the right child of our current root the new root
                self.root = self.root.right
                # delete the previous root
                del temp
            else:
                # if the root has 2 childs then traverse the right branch to find the minimum (leftmost) node keeping track of its parent 
                min_parent = self.root
                min_node = self.root.right
                while min_node.left is not None:
                    min_parent = min_node
                    min_node = min_node.left
                # copy the data from the minimum (leftmost) node to the root node
                self.root.data = min_node.data
                # if minimum node has no right branch
                if min_node.right is None:
                    # make the parent's left node point to None
                    min_parent.left = None
                else:
                    # make minimum's right node the parent's left node
                    min_parent.left = min_node.right
                # delete the minimum node
                del min_node
            # decrease the size of our binary tree
            self.__size -= 1
        else:
            # start from the root
            current = self.root
            # traverse the binary tree until we reach a leaf node or we find the required node
            while current is not None and current.data != item:
                # keep track of the parent node
                parent = current
                if item < current.data:
                    current = current.left
                else:
                    current = current.right
            # if the required item was not found
            if current is None:
                print("Item not found in the binary tree!")
            else:
                # if current node has no child nodes
                if current.left is None and current.right is None:
                    # if the current node happens to be the parent's left node
                    if current.data < parent.data:
                        # make parent left node point to None
                        parent.left = None
                    else:
                        # make parent right node point to None
                        parent.right = None
                elif current.left is not None and current.right is None:
                    # if current node has only one left child then check if the current node is parent's left node
                    if current.data < parent.data:
                        # make current's left node the parent left node
                        parent.left = current.left
                    else:
                        # make current's left node the parent right node
                        parent.right = current.left
                elif current.left is None and current.right is not None:
                    # if current node has only one right child then check if the current node is parent's left node
                    if current.data < parent.data:
                        # make current's right node the parent left node
                        parent.left = current.right
                    else:
                        # make current's right node the parent right node
                        parent.right = current.right
                else:
                    # if current node has 2 childs then traverse the right branch to find the minimum (leftmost) node keeping track of its parent 
                    min_parent = current
                    min_node = current.right
                    while min_node.left is not None:
                        min_parent = min_node
                        min_node = min_node.left
                    # copy the data from the minimum (leftmost) node to the current node
                    current.data = min_node.data
                    # if minimum node has no right branch
                    if min_node.right is None:
                        # make the parent's left node point to None
                        min_parent.left = None
                    else:
                        # make minimum's right node the parent's left node
                        min_parent.left = min_node.right
                    # delete the minimum node
                    del min_node
                # delete the current node
                del current
                # decrease the size of our binary tree
                self.__size -= 1
    
    def __len__(self):
        return self.__size

    def __str__(self):
        pass

# testing our binary tree
def test_binary_tree():
    pass

if __name__ == "__main__":
    test_binary_tree()


         
            