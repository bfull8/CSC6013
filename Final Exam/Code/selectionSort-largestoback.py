def selectionSort(A):
    for i in range(len(A) - 1,0,-1):
        maxIndex = i
        for j in range(i-1,-1,-1):
            if A[j] > A[maxIndex]:
                maxIndex = j
        A[maxIndex], A[i] = A[i], A[maxIndex]

A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
selectionSort(A1)
print(A1)
