import random

def QuickSelect(A,k,left,right):
    """
    Returns the k-th smallest element in the array
    Inputs:
        -A: Array of integers
        -k: Integer that represents the k-th smallest element to search for
    Output:
        -Integer: The value of the k-th smallest element
    """

    # Assign the right element as the pivot
    pivot = A[right]
    # Assign pointer to left index
    p = left

    # For each element from the left to before pivot, compare values to pivot
    for i in range(left,right):
        # If the element is <= pivot, swap larger element with smaller element
        if A[i] <= pivot:
            A[p], A[i] = A[i], A[p]
            p += 1 # increment pointer

    # End with swapping pivot and pointer elements
    A[p], A[right] = A[right], A[p]

    # If k-1 != pointer, call quickselect again on the side of the array where k will be
    if p > (k-1):
        return QuickSelect(A,k,left,p - 1)
    elif p < (k-1):
        return QuickSelect(A,k,p + 1,right)
    else:
        return A[p]


def main():

    # Array of 1000 unique integers between 1 and 100,000
    A = random.sample(range(1, 100001), 1000)

    # Ask user for k (k-th smallest element to search for)
    while True:
        k = int(input("Enter k to find the k-th smallest element: "))
        if k >= 1 and k <= len(A):
            break
        else:
            print(f"Error: Enter a value between 1 and {len(A)}.")

    # Call quickselect and print the k-th smallest element
    print(f"The {k}-th smallest element in the array is: {QuickSelect(A,k,0,len(A)-1)}")

if __name__ == '__main__':
    main()
