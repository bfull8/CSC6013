def quickSelect(A,left,right,k):

    i = left
    pivot = A[right]

    for j in range(left,right):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i+=1


    A[i], A[right] = A[right], A[i]

    if i < k-1:
        return quickSelect(A,i+1,right,k)
    elif i > k-1:
        return quickSelect(A,left,i-1,k)
    else:
        return A[i]

A = [1,2,3,4,5,6]
k=5
print(quickSelect(A,0,len(A)-1,k))
