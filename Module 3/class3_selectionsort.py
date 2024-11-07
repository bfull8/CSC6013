def selectionSort(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1,len(A)):
            if (A[j] < A[minIndex]):
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]


A = [5,3,3,1,2]
selectionSort(A)
