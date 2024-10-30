def smallestGap(A):
    """ Returns an integer indicating the number of integers in an array that are divisible by n
    Inputs:
        A - array of Reals

    Output: Non-Negative Real indicating smallest gap between entries in arrray
    """

    smallest_gap = float('inf')

    for i in range(len(A) - 1):
        for j in range(i+1,len(A)):
            gap = abs(A[i] - A[j])
            if gap < smallest_gap:
                smallest_gap = gap

    return smallest_gap



def main():
    # Test Instance 1
    print(smallestGap([50, 120, 250, 100, 20, 300, 200]))

    # Test Instance 2
    print(smallestGap([12.4, 45.9, 8.1, 79.8, -13.64, 5.09]))

if __name__ == '__main__':
    main()
