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
    print(f"Merge Arrays: Input Arrays = {left} and {right} -> Output Array = {result}")
    return result


def mergeSort(A):
    if len(A) <= 1:
        print(f"Base Case Reached: {A[0]} returned")
        return A
    else:
        mid = len(A) // 2

        print(f"Split Array: Input Array = {A} -> Output Arrays = {A[:mid]} and {A[mid:]}")
        left = mergeSort(A[:mid])
        right = mergeSort(A[mid:])
        output = merge(left,right)
        return output

def main():
    # Test instance 1
    A = [127, 48, 62, 51, 198, 17, 52, 209]
    mergeSort(A)



if __name__ == '__main__':
    main()
