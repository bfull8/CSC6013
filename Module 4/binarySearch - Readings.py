def binarySearch(A,n,low,high):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        if A[mid] < n:
            return binarySearch(A,n,mid+1,high)
        elif A[mid] > n:
            return binarySearch(A,n,low,mid - 1)
        else:
            return mid



sorted = [1,2.3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binarySearch(sorted,6,0,len(sorted) -1))
