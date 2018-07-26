"""
-------------------------
Created on Jul 26, 2018

@author: Prashant Gurung
-------------------------

Linear Search Implementation

"""

# function to sequentially search for an item in a list of items
def linear_search(search_item, items):
    assert type(items) == list, "Second argument items must be a list!"
    # for each item in list of items
    for item in items:
        # check if current item is the search item
        if search_item == item:
            # if it is then return True denoting that item exists in the list
            return True
    # if search item was not found in the list of items then return False
    return False

def main():
    # initialize a list of fruits
    fruits = ["apple", "mango", "orange", "banana", "papaya", "strawberry", "guava"]
    # ask for a fruit name to search
    search_fruit = input("Enter fruit name to search?\n")
    # check if the search_fruit exists in the list of fruits
    if linear_search(search_fruit, fruits) == True:
        print("Search item found!")
    else:
        print("Search item not found!")

if __name__ == "__main__":
    main()
