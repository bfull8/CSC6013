def quickSelect(A,left,right,k):

    i = left
    pivot = A[right]

    for j in range(left,right):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i+=1

    A[right],A[i] = A[i], A[right]

    if i > k:
        return quickSelect(A,left,i-1,k)
    elif i < k:
        return quickSelect(A,i+1,right,k)
    else:
        return A[i]

A = [3,2,1,5,6,4]
print(quickSelect(A,0,len(A)-1,len(A)-2))
