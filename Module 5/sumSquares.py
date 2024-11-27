def sumSquares(n):
    """
    Calculates the sum of squares of positive Integer n
    Input:
        n: Positive Integer
    Output:
        Integer representing the sum of squares of n
    """

    # Base Case
    if n == 1:
        return 1
    # Recursive Case
    else:
        return n**2 + sumSquares(n-1)

def main():

    # Test Instance 1
    print(f"n = 12: {sumSquares(12)}")

    # Test Instance 2
    print(f"n = 20: {sumSquares(20)}")

if __name__ == '__main__':
    main()
