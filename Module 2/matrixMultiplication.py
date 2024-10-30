def multiplyMatrices(A,B,n):
    """ Returns an integer indicating the number of integers in an array that are divisible by n
    Inputs:
        A - 2D array representing Matrix 1
        B - 2D array representing Matrix 2
        n - Positive integer representing size of square matrices

    Output: 2D array representing product of AB
    """
    C = []

    row = []
    i,j = 0,0
    while i < range(n):
        product = 0
        while j < range(n):
            product += A[i][j] * B[j][i]
        row.append(product)
    C.append(row)

    return C


A = [[2,7],[3,5]]
B = [[8,-4],[6,6]]

print(multiplyMatrices(A,B,2))
