# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return 1
        else:
            return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Base case of empty list/array
    if len(arr) == 0:
        return -1  # array empty
    # These variables correspond to the highest/lowest indicies avail
    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    # Loop until value found
    while low <= high:
        # Find the middle index, rounded down if neccessary
        middle = (low+high)//2
        # Check which side of the middle the target falls
        ''' Change the value of the low or high to reflect
        which side targets on'''
        if target < arr[middle]:
            # Eliminate higher side of array
            high = middle-1
        elif target > arr[middle]:
            # Eliminate lower side of array
            low = middle+1
        else:
            # Returns index of found value
            return middle
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)/2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
