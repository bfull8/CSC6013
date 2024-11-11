def selectionSort(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1,len(A)):
            if (A[j] < A[minIndex]):
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]


A = [5,3,3,1,2]
selectionSort(A)


def selection_sort_descending_trace(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        comparisons = 0
        swaps = 0

        # Find the index of the largest element in the unsorted portion
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap if max_index is not the current position i
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            swaps += 1

        # Print the number of comparisons, swaps, and current status of the array
        print(f"Iteration {i + 1}: Comparisons = {comparisons}, Swaps = {swaps}, Array = {arr}")

# Test arrays
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

# Run the algorithm on each test array
print("Sorting A1:")
selection_sort_descending_trace(A1)
print("\nSorting A2:")
selection_sort_descending_trace(A2)
print("\nSorting A3:")
selection_sort_descending_trace(A3)
