def countBinaryDigits(n):
    # Base Case
    if n == 1:
        return 1
    else:
        return 1 + countBinaryDigits(n // 2)


print(countBinaryDigits(256))
print(countBinaryDigits(750))

# T(n) = 1 + T(n/2)
