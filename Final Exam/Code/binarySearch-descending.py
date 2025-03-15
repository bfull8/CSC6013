def binarySearch(A,start,end,k):
    if start > end:
        return None
    else:
        mid = (start+end)//2
        if A[mid] == k:
            return mid
        elif A[mid] < k:
            return binarySearch(A,start,mid-1,k)
        else:
            return binarySearch(A,mid+1,end,k)

A1 = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]
print(binarySearch(A1,0,len(A1)-1,44))
