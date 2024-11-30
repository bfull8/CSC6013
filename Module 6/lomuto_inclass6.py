def lomuto(A,left,right):
    p = A[right]
    i = left

    print("Step 1")
    print(f"i = 0, j = 0")
    print(f"Pivot at index {right}: {p}")
    print(f"Elements lesser than pivot: {A[0:0]}")
    print(f"Elements greater than pivot: {A[i:0]}")
    print(f"Elements still to be sorted: {A[0:right]}")
    print()

    total_swaps = 0
    for j in range(right):
        swap = 0
        if A[j] < p:
            swap += 1
            total_swaps += 1
            ai = A[i]
            aj = A[j]
            A[j], A[i] = A[i], A[j]
            i += 1


        print(f"Step {j+2}:")
        if swap == 0:
            print(f"i = {i}, j = {j} -> i = {i}, j = {j+1}")
        else:
            print(f"i = {i -1}, j = {j} -> i = {i}, j = {j+1}")

        if swap == 0:
            print(f"A[j]: {A[j]} > Pivot: {p}, no swap made | Total swaps = {total_swaps}")
        else:
            print(f"A[j]: {aj} <= Pivot: {p}, swap A[i]: {ai} with A[j]: {aj} | Total swaps = {total_swaps}")

        print(f"Elements lesser than pivot: {A[0:i]}")
        print(f"Elements greater than pivot: {A[i:j+1]}")
        print(f"Elements still to be sorted: {A[j+1:right]}")
        print()

    print(f"Step 12:")
    print(f"Swap A[i]: {A[i]} with Pivot: {p} | Total swaps = {total_swaps + 1}")
    A[i], A[right] = A[right], A[i]
    print(f"Elements lesser than pivot: {A[0:i]}")
    print(f"Elements greater than pivot: {A[i:j+1]}")
    print(f"Pivot: {A[i]} at index {i}")
    return i

A = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
pvt = lomuto(A,0,len(A)-1)
print()
print(f"Final Array: Lomuto with pivot at index {pvt}: {A[pvt]}")
print(A)
