"""
-------------------------
Created on Jul 27, 2018

@author: Prashant Gurung
-------------------------

Merge Sort Implementation

"""

# function to merge two sorted lists
def merge_sorted_lists(list1, list2):
    assert type(list1) == list and type(list2) == list, "Arguments list1 and list2 must both be of type list!"
    # initialize new merged list
    merged_list = []
    # initialize index pointer for list1
    index1 = 0
    # initilize index pointer for list2
    index2 = 0
    # loop until we go through each of the item in both lists
    while index1 < len(list1) or index2 < len(list2):
        # if there is an item left to consider in list1 but no items left to consider in list2
        if index1 < len(list1) and index2 == len(list2):
            # append the item from list1 to the merged list
            merged_list.append(list1[index1])
            # increase index1 by 1
            index1 += 1
        # if there is an item left to consider in list2 but no items left to consider in list1
        elif index1 == len(list1) and index2 < len(list2):
            # append the item from list2 to the merged list
            merged_list.append(list2[index2])
            # increase index2 by 1
            index2 += 1
        # if there are items left to consider in both lists and the item in list1 is less than or equal to item in list2
        elif list1[index1] <= list2[index2]:
            # append the item from list1 to the merged list
            merged_list.append(list1[index1])
            # increase index1 by 1
            index1 += 1
        # if there are items left to consider in both lists and the item in list2 is less than the item in list1
        else:
            # append the item from list2 to the merged list
            merged_list.append(list2[index2])
            # increase index2 by 1
            index2 += 1
    # return the new merged list
    return merged_list

# function to return a sorted list of items given an unsorted list of items
def merge_sort(items):
    assert type(items) == list, "Argument items must be a list!"
    # if the list is empty or has only one item then return it
    if len(items) <= 1:
        return items
    else:
        # calculate the mid index to divide the list
        mid = len(items) // 2
        # divide the list into two halves and recursively call merge_sort for those two halves
        lower_half = merge_sort(items[:mid])
        upper_half = merge_sort(items[mid:])
        # finally return the two halves by merging them
        return merge_sorted_lists(lower_half, upper_half)

def main():
    # make our test list of 1000 numbers
    test_list = []
    for i in range(1000):
        test_list.append(1000 - i)
    # sort the test list using merge sort
    sorted_list = merge_sort(test_list)
    # print the sorted list
    print(sorted_list)

if __name__ == "__main__":
    main()

        
