def quicksort_descending(arr, low, high):
    global swap_count, call_count
    call_count += 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort_descending(arr, low, pi-1)
        quicksort_descending(arr, pi+1, high)

def partition(arr, low, high):
    global swap_count
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]
            swap_count += 1

    # Place pivot in correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    swap_count += 1
    return i+1

# Test arrays
A = [38, 21, 39, 60, -1, 10, 81, 23]
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

def test_quicksort(arr):
    global swap_count, call_count
    swap_count = 0
    call_count = 0
    arr_copy = arr.copy()
    quicksort_descending(arr_copy, 0, len(arr_copy) - 1)
    print(f"Array: {arr}")
    print(f"Sorted: {arr_copy}")
    print(f"Number of swaps: {swap_count}")
    print(f"Number of recursive calls: {call_count}")
    print()

# Test the function on all arrays
test_quicksort(A)
test_quicksort(B)
test_quicksort(C)
