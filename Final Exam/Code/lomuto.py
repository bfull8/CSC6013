def lomuto(A,left,right):
    i = left
    pivot = A[right]

    for j in range(left,right):
        if A[i] < pivot:
            A[i], A[j] = A[j], A[i]
            i +=1

    A[i], A[right] = A[right], A[i]
    return i

A = [31,55,19,13,42,6,60,36,48,24]
A.sort()
pvt = lomuto(A,0,len(A)-1)
print(pvt)
print(A)
