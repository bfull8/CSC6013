def bubbleSort(A):
    for i in range(len(A)-1):
        swap = 0
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                A[j],A[j+1] = A[j+1],j
                swap += 1
        if swap == 0:
            break

A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
bubbleSort(A4)
print(A4)
