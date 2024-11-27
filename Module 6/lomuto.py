def lomuto(A,left,right):
    p = A[right]
    i = left
    for j in range(left,right):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]

    return i

A = [31,55,19,13,42,6,60,36,38,24]
lomuto(A,0,len(A)-1)
print(A)
