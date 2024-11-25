def binaryDigits(n):
    if n == 1:
        return 1
    else:
        return 1 + binaryDigits(n//2)

def main():

    # Test Instance 1
    print(f"n = 256: {binaryDigits(256)} digits")

    # Test Instance 2
    print(f"n = 750: {binaryDigits(750)} digits")

if __name__ == '__main__':
    main()