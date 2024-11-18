# Ben Fullenkamp
# CSC6013 - Project 4

def binSearch(A,start,end,k):
    """
    Returns the index of where k appears in array A
    Inputs: A     - Array sorted in descending order
            start - Start index
            end   - End index
            k     - Number to search
    Ouput: Index where k appears in array A
    """

    # Calculate the mid point
    mid = (start + end) // 2

    # Continue splitting the array in half until k is found or None is returned
    if start > end:
        # Print the subarray to show it is empty then return None
        print(f"Array = {A[start:end+1]} | Mid = {None}")
        return None
    else:
        # Print the subarray and it's midpoint
        print(f"Array = {A[start:end+1]} | Mid = {A[mid]}")
        if A[mid] == k:
            return mid
        elif A[mid] > k:                            # if k is less than the mid element, return the right side of the array
            return binSearch(A,mid+1,end,k)
        else:                                       # if k is greater than the mid element, return the left side of the array
            return binSearch(A,start,mid-1,k)

def main():
    A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
    A2 = [9, 7, 6, 4, 2, 0, -1, -3, -5, -8, -9]

    # Test Instance 1 - Searching for 44:
    i = 44
    print(f"Searching for {i}:")
    print(f"{i} is at index {binSearch(A1,0,len(A1)-1,i)}")
    print()

    # Test Instance 2 - Searching for 56:
    i = 56
    print(f"Searching for {i}:")
    print(f"{i} is at index {binSearch(A1,0,len(A1)-1,i)}")
    print()

    # Test Instance 3 - Searching for 42:
    i = 42
    print(f"Searching for {i}:")
    print(f"{i} is at index {binSearch(A1,0,len(A1)-1,i)}")
    print()

    # Test Instance 4 - Searching for -1:
    i = -1
    print(f"Searching for {i}:")
    print(f"{i} is at index {binSearch(A2,0,len(A2)-1,i)}")
    print()

    # Test Instance 5 - Searching for -7:
    i = -7
    print(f"Searching for {i}:")
    print(f"{i} is at index {binSearch(A2,0,len(A2)-1,i)}")

if __name__ == '__main__':
    main()
