def merge(left,right):
    result, i, j = [],0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:] # Still elements left in the left array, so nothing to compare to
    result += right[j:] # Still elements left in the right array, so nothing to compare to
    return result

def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        # Recursion
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])

        return merge(left,right)


A = [2,3,5,1,7,4,4,4,2,6,0]
print(mergeSort(A))
