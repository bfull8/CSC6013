# Ben Fullenkamp
# CSC6013 - Project 4

def minElement(A,start,end):
    """
    Returns the index of the minimum element in the array
    Inputs:
        A - Unsorted array
        Start - Start index
        End - End index
    Output: Index of the minimum element in A
    """

    # Print the start and end values
    print(f"A[{start}:{end}], Start = {A[start]}, End = {A[end]}")

    # If a single element is remaining, return it
    if start == end:
        print(f"Base Case Reached: {A[end]} returned")
        return end
    else:
        mid = (start + end) // 2
        fst = minElement(A,start,mid)
        lst = minElement(A,mid+1,end)

        # Compare the left and right side of subarray and return the minimum
        min = fst if A[fst] < A[lst] else lst
        print(f"Return minimum between {A[fst]} and {A[lst]}: {A[min]} returned")
        return min


def main():
    # Test arrays
    A1 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
    A2 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
    A3 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

    # Test Instance 1:
    i = minElement(A1,0,len(A1)-1)
    print("---------------------------------------------")
    print(f"The minimum number is {A1[i]} at index {i}")
    print()

    # Test Instance 2:
    i = minElement(A2,0,len(A2)-1)
    print("---------------------------------------------")
    print(f"The minimum number is {A2[i]} at index {i}")
    print()

    # Test Instance 3:
    i = minElement(A3,0,len(A3)-1)
    print("---------------------------------------------")
    print(f"The minimum number is {A3[i]} at index {i}")

if __name__ == '__main__':
    main()
