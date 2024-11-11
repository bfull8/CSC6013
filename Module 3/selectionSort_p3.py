# Ben Fullenkamp
# CSC6013 - Project 3

def selectionSort(A):
    """ Sort the array with largest elements going into the last position first
        Input - Array of integers
        Output - Sorted array
    """

    # Decrement the index value to compare elements from right to left
    # Swap elements once the largest element to the left is found
    for i in range(len(A) - 1,0,-1):
        maxIndex = i    # Holds largest element index for each iteration
        swap = 0        # Counter for number of swaps
        compare = 0     # Counter for number of comparisons
        for j in range(i - 1, -1,-1):
            compare += 1
            if A[maxIndex] < A[j]:
                maxIndex = j
                swap = 1
        A[i], A[maxIndex] = A[maxIndex], A[i]

        # Print the number of comparisons, swaps, and current status of the array
        print(f"Comparisons = {compare} | Swaps = {swap} | Array = {A}")

    return A

def main():

    # Three test arrays
    A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
    A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
    A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

    # Test Array 1
    selectionSort(A1)
    print(f"\n{"-"*140}\n")

    # Test Array 2
    selectionSort(A2)
    print(f"\n{"-"*140}\n")

    # Test Array 3
    selectionSort(A3)


if __name__ == '__main__':
    main()
