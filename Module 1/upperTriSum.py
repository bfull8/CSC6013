def UpperTriangularSum(A,n):
    sum = 0
    for i in range(n):
        for j in range(i,n):
            sum += A[i][j]
    return sum

A = [[1,2],[0,2]]
print(UpperTriangularSum(A,2))
