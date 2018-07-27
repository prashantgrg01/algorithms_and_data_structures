"""
-------------------------
Created on Jul 27, 2018

@author: Prashant Gurung
-------------------------

Insertion Sort Implementation

"""

# function to return a sorted list of items given an unsorted list of items
def insertion_sort(items):
    assert type(items) == list, "Argument items must be a list!"
    # loop through each item starting from the second item
    for i in range(1, len(items)):
        # make current item the key
        key = items[i]
        # adjust j for comparing the key with items on its left side
        j = i - 1
        # loop until we get to an item on the left side that is greater than or equal to the key item
        while j >= 0 and key < items[j]:
            # move the current left item one step to the right
            items[j+1] = items[j]
            # decrease j by one to compare the key with the next left item
            j = j - 1
        # store the key in its rightful position
        items[j+1] = key
    # return the sorted list
    return items

def main():
    # make our test list of 1000 numbers
    test_list = []
    for i in range(1000):
        test_list.append(1000 - i)
    # sort the test list using insertion sort
    sorted_list = insertion_sort(test_list)
    # print the sorted list
    print(sorted_list)

if __name__ == "__main__":
    main()
            