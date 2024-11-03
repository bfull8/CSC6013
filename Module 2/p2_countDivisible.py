def countDivisble(A,n):
    """ Returns an integer indicating the number of integers in an array that are divisible by n
    Inputs:
        A - array of integers
        n - positve integer
    Output: Integer indicating number of entries in array divisible by n
    """

    # Initialize a variable to hold the count
    count = 0

    # Loop through each integer in the array
    # Increment the count if there is no remainder after dividing it by n
    for num in A:
        if num % n == 0:
            count += 1

    # Return the count
    return count

def main():
    # Number of entries divisible by 7
    print(f"Test Instance 1: {countDivisble([20, 21, 25, 28, 33, 34, 35, 36, 41, 42],7)}")

    # Number of entries divisible by 9
    print(f"Test Instance 2: {countDivisble([18, 54, 76, 81, 36, 48, 99],9)}")

if __name__ == '__main__':
    main()
