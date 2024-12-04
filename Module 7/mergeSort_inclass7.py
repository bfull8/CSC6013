def merge(left,right):
    result,i,j = [],0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    print(f"Input Arrays = {left} and {right} | Output Array = {result}")
    return result


def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])
        output = merge(left,right)
        return output

def main():
    # Test instance 1
    A = [38, 21, 39, 60, -1, 10, 81, 23]
    mergeSort(A)
    # Test Instance 2
    print()
    print()
    B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
    mergeSort(B)
    # Test Instance 3
    print()
    print()
    C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
    mergeSort(C)


if __name__ == '__main__':
    main()
