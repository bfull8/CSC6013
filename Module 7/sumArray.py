def sumArray(A,start,end):

    mid = (start+end) // 2
    if start == end:
        return A[start]
    else:
        return sumArray(A,start,mid) + sumArray(A,mid+1,end)

A = [1,4,2,3,1,6,7,1]
print(sumArray(A,0,len(A)-1))
