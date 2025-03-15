def findMode(A):
    A.sort()

    mode = None
    mode_count = 0

    current_value = A[0]
    current_count = 1

    for i in range(1,len(A)):
        if A[i] == current_value:
            current_count += 1
        else:
            if current_count > mode_count:
                mode = current_value
                mode_count = current_count

            current_value = A[i]
            current_count = 1

    if current_count > mode_count:
        mode = current_value

    return mode

A = [1,2,3,2,2,4,5,5,5]
findMode(A)
