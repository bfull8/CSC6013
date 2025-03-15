def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-i-1): #Shrinks by 1 each time (just like when we do range(i,len(A))
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

A = [6,5,3,1,8,7,2,4]
bubbleSort(A)
print(A)
