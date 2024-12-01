def lomuto(A,left,right):
    pivot = A[right]
    i = left
    for j in range(left,right):
        if A[j] < pivot:
            A[j], A[i] = A[i],A[j]
            i += 1

    # Swap pivot
    A[i], A[right] = A[right], A[i]

    return i # Pivot element after first step of quick sort



def quickSort(A, left, right):
    if left < right: # Subarray contains at least 2 elements. If len(A) = 1, you do nothing
        mid = lomuto(A,left,right)
        quickSort(A,left,mid-1) # All elements less than pivot element
        quickSort(A,mid+1,right)   # All elements greater than pivot element

A = [22,11,88,66,55,77,33,44]
quickSort(A,0,len(A)-1)
print(A)
