def binaryDigits(n):
    """
    Calculates the number of digits in the binary expansion/representation of a positive Integer n
    Input:
        n: Postive Integer
    Output:
        Integer representing the number of binary digits in binary representation of n
    """

    # Base Case
    if n == 1:
        return 1
    # Recursive case
    else:
        return 1 + binaryDigits(n//2)

def main():

    # Test Instance 1
    print(f"n = 256: {binaryDigits(256)} digits")

    # Test Instance 2
    print(f"n = 750: {binaryDigits(750)} digits")

if __name__ == '__main__':
    main()
