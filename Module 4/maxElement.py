from random import randint

def Max(A, start, end):
    if (start == end):
        return end
    else:
        mid = (end + start) // 2
        fst = Max(A, start, mid)
        lst = Max(A, mid + 1, end)
        max = fst if A[fst] > A[lst] else lst
        return max

#A = [randint(0,10000) for _ in range(8)]
A = [27,14,3,8,17,5,25,1]
i = Max(A,0,len(A)-1)
print(A,A[i],i)
