def maxElement(A,start,end):
    if start == end:
        return end
    else:
        mid = (start + end)//2
        fst = maxElement(A,start,mid)
        lst = maxElement(A,mid+1,end)
        if A[fst] > A[lst]:
            return fst
        else:
            return lst

A = [27,14,3,8,17,5,25,1]
print(maxElement(A,0,len(A)-1))
