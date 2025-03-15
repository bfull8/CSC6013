def insertionSort(A):
    for i in range(len(A)-2,-1,-1):
        for j in range(len(A)-1,i,-1):
            if A[i] > A[j]:
                A.insert(j,A.pop(i))
                break

A = [8,11,8,3,5,10]
insertionSort(A)
print(A)
