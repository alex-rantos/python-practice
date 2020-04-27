import numpy as np

def partition(arr, low, high): 
    i = (low - 1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller  
        # than or equal to pivot 
        if arr[j] <= pivot: 
          
            # increment index of 
            # smaller element 
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 
  
# Function to do Quick sort 
def quicksort(arr, low, high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi + 1, high) 
    
# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def quicksort_iterative(arr, l, h): 
  
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

if __name__ == "__main__":
    arr = np.array([2,7,4,1,8,1])
    sorted_arr = quicksort_iterative(arr,0,len(arr) - 1)
    arr.sort()
    assert (sorted_arr == arr.sort())