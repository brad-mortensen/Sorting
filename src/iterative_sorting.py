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
    # Iterates backwards through the range of the length of the arr
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


arr = [23, 978906, 236, 27, 78, 8976, 252, 54, 7870]
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
