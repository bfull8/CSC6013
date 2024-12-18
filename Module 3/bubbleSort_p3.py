# Ben Fullenkamp
# CSC6013 - Project 3

def bubbleSort(A):
    """ Sorts an array by comparing adjacent elements and swapping if they are out of order
        Input - Array of integers
        Output - Sorted Array
    """

    # Compare each element to its neighbor on the right and swap if the neighbor is smaller
    for i in range(len(A) - 1):
        compare = 0         # Counter for number of comparisons
        swap = 0            # Counter for number of swaps
        for j in range(len(A) - i - 1):
            compare += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap += 1

        # Print the number of comparisons, swaps, and current status of the array
        print(f"Comparisons = {compare} | Swaps = {swap} | Array = {A}")

        # If there were no swaps in the iteration, the array is already sorted
        if swap == 0:
            return

def main():

    # Three test arrays
    A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

    # Test Array 1
    bubbleSort(A4)
    print(f"\n{"-"*140}\n")

    # Test Array 2
    bubbleSort(A5)
    print(f"\n{"-"*140}\n")

    # Test Array 3
    bubbleSort(A6)

if __name__ == '__main__':
    main()
