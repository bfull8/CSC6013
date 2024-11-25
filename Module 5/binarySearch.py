def binSearch(A,start,end,k):
    mid = (start + end) // 2
    if start > end:
        return None
    elif k == A[mid]:
        return mid
    elif k < A[mid]:
        return binSearch(A,start,mid-1,k)
    else:
        return binSearch(A,mid +1, end, k)

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(binSearch(A,0,len(A)-1,6))
