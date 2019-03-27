# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            # Loops through remaining elements
            if arr[cur_index] > arr[j]:
                cur_index = j
        # TO-DO: swap
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Iterate backwards through the range list length
    for i in range(len(arr)-1, 0, -1):
        # Iterate through remaining indicies
        for j in range(i):
            # Check if item at j is bigger than item at j+1 index
            if arr[j] > arr[j+1]:
                # If item at j is larger, save to temporary var
                temp = arr[j]
                # Assign smaller item to current index
                arr[j] = arr[j+1]
                # Assign temp var to item at j+1 index
                arr[j+1] = temp
    return arr


arr = [23, 978906, 236, 27, 78, 8976, 252, 54, 7870]
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below

''' https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
is how I got this weird sort :).'''


def count_sort(arr, maximum=-1):
    # Add one to the maximum input
    max_key = maximum + 1
    # Create a list with max+1 idicies all zero valued
    count = [0] * max_key
    # Count the occurances of each number and increment num at that index
    for counts in array:
        count[counts] += 1
    # Set a counter variable to handle reordered array indicies
    i = 0
    # Loop range of max_key times for outer loop
    for val in range(max_key):
        # Loop through counting array and assign those values to
        # [i]index of sorted array
        for idx in range(count[val]):
            arr[i] = val
            # Increment counting var
            i += 1
    return arr
