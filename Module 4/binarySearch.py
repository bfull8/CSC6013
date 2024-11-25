def binSearch(A,start,end,k,count):
    mid = (start + end) //2
    if start > end:
        return None, count
    elif (A[mid] == k):
        return mid, count
    elif (A[mid] > k):
        count +=1
        return binSearch(A,start, mid - 1, k,count)
    else:
        count +=1
        return binSearch(A,mid + 1, end, k,count)
