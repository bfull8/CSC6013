recursive_calls = 0
swaps = 0

def lomuto(A,left,right):
    """
    Partitions the Array where each element to the left of the pivot is greater than the pivot element
    and each element to the right is less than the pivot element

    Inputs:
        A - The Array to be partitioned
        left - Left index of the array
        right - Right index of array
    Output: Integer representing the index of the pivot element after partitioning
    """
    # Variable to keep track of total swaps
    global swaps

    # Assign the pivot as the last element and the pointer as the first element of the array
    pivot, i = A[right], left

    # Increment through each element in the array up to the element before the pivot
    # If the element is greater than the pivot, swap the element with the pointer
    for j in range(left,right):
        if A[j] > pivot:
            A[j], A[i] = A[i], A[j]
            i += 1                  # Increment the pointer
            swaps += 1

    # Swap the pivot with the pointer element at the end of all swaps
    A[i], A[right] = A[right], A[i] # count the pivot swap
    # Return the pivot index
    return i

def QuickSort(A,left,right):
    """
        Partitions the Array until all elements are in descending order
        Inputs:
            A - The Array to be sorted
            Left - Left index of Array
            Right - Right index of Array
        Output: N/A - Sorts the Array in-place
    """
    # Variable to keep track of total swaps
    global recursive_calls
    recursive_calls += 1
    # If the Array has 2 or more elements, partition each half of the array
    # Otherwise, do nothing
    if left < right:
        mid = lomuto(A,left,right)
        QuickSort(A,left,mid-1)
        QuickSort(A,mid+1,right)

def main():
    global recursive_calls
    global swaps

    # Test Instance 1
    A = [38, 21, 39, 60, -1, 10, 81, 23]
    QuickSort(A,0,len(A)-1)
    print(f"Final sorted array: {A} | Total Swaps = {swaps} | Total Recursive Calls = {recursive_calls}")

    # Test Instance 2
    # Reset trace variables
    recursive_calls = 0
    swaps = 0
    B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
    QuickSort(B,0,len(B)-1)
    print(f"Final sorted array: {B} | Total Swaps = {swaps} | Total Recursive Calls = {recursive_calls}")

    # Test Instance 3
    # Reset trace variables
    recursive_calls = 0
    swaps = 0
    C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
    QuickSort(C,0,len(C)-1)
    print(f"Final sorted array: {C} | Total Swaps = {swaps} | Total Recursive Calls = {recursive_calls}")

if __name__ == '__main__':
    main()
