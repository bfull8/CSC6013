def multiplyMatrices(A,B,n):
    """ Multiplies two square matrices with size n dimensions
    Inputs:
        A - 2D array representing Matrix 1
        B - 2D array representing Matrix 2
        n - Positive integer representing size of square matrices

    Output: 2D array representing product of AB
    """

    # Initialize variable to hold product matrix
    C = []

    # Loop through each element in matrix A and B
    # Calculate dot product for each row in A by each column in B
    for i in range(n):
        row = []
        for j in range(n):
            product = 0
            for k in range(n):
                product += A[i][k] * B[k][j]
            row.append(round(product,2))
        C.append(row)

    # Return product matrix
    return C


def main():

    # Test Instance 1
    A = [[2,7],[3,5]]
    B = [[8,-4],[6,6]]

    print(f"Test Instance 1: {multiplyMatrices(A,B,2)}")

    # Test Instance 2
    A = [[1,0,2],[3,-2,5],[6,2,-3]]
    B = [[.3,.25,.1],[.4,.8,0],[-.5,.75,.6]]

    print(f"Test Instance 2: {multiplyMatrices(A,B,3)}")

if __name__ == '__main__':
    main()
