"""
-------------------------
Created on Jul 20, 2018

@author: Prashant Gurung
-------------------------

Hash Table Implementation using Chaining for resolving collisions and DJB2 Hash Algorithm for hashing keys

Methods:
is_empty() => O(1) => returns whether the hash table is empty or not
add(key, value) => O(1) => adds the given (key, value) pair to the hash table and if the key exists it only overrides its value
remove(key) => O(1) => removes the given key from the hash table
get(key) => O(1) => searches for the given key in the hash table and returns its value if found else an error

"""

# Class definition for Hash Table
class HashTable(object):
    def __init__(self, size):
        # initialize the size of our hash table
        self.size = size
        # create a hash table with given size
        self.table = [None] * self.size
        # initialize the number of entries in our hash table
        self.entries = 0

    # Implementation of Hash Function using DJB2 Hash Algorithm
    def djb2_hash(self, key):
        hash_value = 5381
        for char in key:
            hash_value = hash_value * 33 + ord(char)
        return hash_value

    def is_empty(self):
        return self.entries == 0
    
    def add(self, key, value):
        # generate hash for the given key
        hash_value = self.djb2_hash(key)
        # calculate the index to store the (key, value) pair
        index = hash_value % self.size
        # check to see if there are no entries at the calculated index
        if self.table[index] is None:
            # create an empty list in that index
            self.table[index] = []
            # add new entry for (key, value) pair to that list
            self.table[index].append([key, value])
            # increase the number of entries in our hash table and return
            self.entries += 1
            return True
        else:
            # check if the key already exists and only update its value and return
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # else append the new entry to the end of the list
            self.table[index].append([key, value])
            # increase the number of entries in our hash table and return
            self.entries += 1
            return True            

    def remove(self, key):
        # generate hash for the given key
        hash_value = self.djb2_hash(key)
        # calculate the index where the key resides
        index = hash_value % self.size
        # check to see if there are entries in the calculated index
        if self.table[index] is not None:
            # check if the key exists in those entries at the index
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    # delete the (key, value) pair from the list of entries
                    del self.table[index][i]
                    # decrease the number of entries in our hash table and return
                    self.entries -= 1
                    return True
        # else return error and return
        print("Error! Key not found.")
        return False

    def get(self, key):
        # generate hash for the given key
        hash_value = self.djb2_hash(key)
        # calculate the index where the key resides
        index = hash_value % self.size
        # check to see if there are entries in the calculated index
        if self.table[index] is not None:
            # check if the key exists in those entries at the index
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    # return the value for the key
                    return self.table[index][i][1]
        # else return error and return
        print("Error! Key not found.")
    
    def __len__(self):
        return self.entries

    def __str__(self):
        # initialize res to empty string
        res = ""
        # for each entry in hash table that is not None, append it to the result as string
        for entry in self.table:
            if entry is not None:
                res += str(entry) + "\n"
        # return the result removing the last new line
        return res[:-1]

# testing our hash table
def test_hash_table():
    pass

if __name__ == "__main__":
    test_hash_table()



    
    















