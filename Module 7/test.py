def merge(left, right):
    result, i, j = [], 0, 0

    print(f"Merging: left={left}, right={right}")  # Print input arrays for merging
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]  # Add remaining elements from `left` if any
    result += right[j:]  # Add remaining elements from `right` if any
    print(f"Result after merge: {result}")  # Print merged result
    return result

def mergeSort(A):
    if len(A) <= 1:
        print(f"Base case: {A}")  # Print base case (single-element array)
        return A
    else:
        mid = len(A) // 2
        print(f"Splitting: {A[:mid]} and {A[mid:]}")  # Print arrays being split

        # Recursive calls
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])

        # Merge results
        return merge(left, right)

def traceMergeSort(A):
    print(f"Tracing MergeSort for array: {A}")
    sorted_array = mergeSort(A)
    print(f"Final sorted array: {sorted_array}\n")

# Test arrays
A = [38, 21, 39, 60, -1, 10, 81, 23]
B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]

# Trace the MergeSort algorithm for each array
traceMergeSort(A)
traceMergeSort(B)
traceMergeSort(C)
