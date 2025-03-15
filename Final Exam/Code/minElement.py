def minElement(A,start,end):
    if start == end:
        return end
    else:
        mid = (start+end)//2
        fst = minElement(A,start,mid)
        lst = minElement(A,mid+1,end)
        if A[fst] < A[lst]:
            return fst
        else:
            return lst

A3 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
print(minElement(A3,0,len(A3)-1))
