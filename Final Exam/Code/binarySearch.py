def binarySearch(A,start,end,k):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            return binarySearch(A,start,mid-1,k)
        else:
            return binarySearch(A,mid+1,end,k)

A = [0,1,2,3,4,5,6,7,9]
print(binarySearch(A,0,len(A)-1,5))
print(binarySearch(A,0,len(A)-1,14))
