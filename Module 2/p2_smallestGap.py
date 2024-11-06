def smallestGap(A):
    """ Returns the smallest gap between all pairs of elements in an Array
    Inputs:
        A - array of Real numbers

    Output: Non-Negative Real indicating smallest gap between entries in array
    """

    # Check that the array has pairs to calculate gap
    if len(A) < 2:
        return "Not enough elements in array to calculate a gap"

    # Initialize a variable to hold the smallest gap
    # Start as infinity so the first gap is calculation is always less than
    smallest_gap = float('inf')

    # Loop through each element in the array and find the gap for each element to the right
    # Overwrite the smallest gap variable if the calculated gap is less than what is stored
    for i in range(len(A) - 1):
        for j in range(i+1,len(A)):
            gap = abs(A[i] - A[j])
            if gap < smallest_gap:
                smallest_gap = gap

    # Return the smallest gap
    return smallest_gap



def main():
    # Test Instance 1
    print(f"Test Instance 1: {smallestGap([50, 120, 250, 100, 20, 300, 200])}")

    # Test Instance 2
    print(f"Test Instance 2: {smallestGap([12.4, 45.9, 8.1, 79.8, -13.64, 5.09])}")

if __name__ == '__main__':
    main()
