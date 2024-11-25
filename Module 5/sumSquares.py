def sumSquares(n):
    # Base Case
    if n == 1:
        return 1
    else:
        return n**2 + sumSquares(n-1)

print(sumSquares(12))
print(sumSquares(20))

# T(n) = 1 + T(n-1)
