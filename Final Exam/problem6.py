def Maximum(A, right):
    if right == 0:
        print(f"Base Case Reached. Return {A[0]}")
        return A[0]
    else:
        max_remaining = Maximum(A, right-1)
        print(f"Compare {max_remaining} and {A[right]}")
        max_so_far = max_remaining if max_remaining > A[right] else A[right]
        print(f"Return {max_so_far}")
        return max_so_far

A = [17, 62, 49, 73, 26, 51]
print(f"Maximum Element: {Maximum(A,len(A)-1)}")
