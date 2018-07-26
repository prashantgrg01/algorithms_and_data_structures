"""
-------------------------
Created on Jul 26, 2018

@author: Prashant Gurung
-------------------------

Binary Search Implementation - Iterative and Recursive

"""

# function to search for an item in a sorted list of items using iterative divide-and-conquer algorithm
def binary_search_iterative(search_item, items):
    assert type(items) == list, "Second argument items must be a list!"
    # initialize our lower and upper bounds
    low = 0
    high = len(items)
    # initialize found to False
    found = False
    # loop until the search item is found or we reach the end of the list
    while not found and low <= high:
        # calculate the mid index
        mid = (low + high) // 2
        # check if the search item is the middle item of the list
        if search_item == items[mid]:
            # if so set found to True
            found = True
        elif search_item < items[mid]:
            # if search item is less than the middle item then only search the lower half next time
            high = mid - 1
        else:
            # if the search item is greater than the middle item then only search the upper half next time
            low = mid + 1
    # return whether the item was found or not as True or False
    return found

# function to search for an item in a sorted list of items using recursive divide-and-conquer algorithm
def binary_search_recursive(search_item, items):
    assert type(items) == list, "Second argument items must be a list!"
    # if the list is empty return False denoting that item was not found
    if len(items) == 0:
        return False
    else:
        # calculate the mid index
        mid = len(items) // 2
        # check if the search item is the middle item of the list
        if search_item == items[mid]:
            # if so return True denoting that item was found
            return True
        elif search_item < items[mid]:
            # if search item is less than the middle item then only search the lower half next time
            return binary_search_recursive(search_item, items[:mid])
        else:
            # if the search item is greater than the middle item then only search the upper half next time
            return binary_search_recursive(search_item, items[mid+1:])

def main():
    # initialize a sorted list of fruits
    fruits = ["apple", "banana", "guava", "mango", "orange", "papaya", "strawberry"]
    # ask for a fruit name to search
    search_fruit = input("Enter fruit name to search?\n")
    # check if the search_fruit exists in the list of fruits
    if binary_search_recursive(search_fruit, fruits) == True:
        print("Search item found!")
    else:
        print("Search item not found!")

if __name__ == "__main__":
    main()



