def hanoi(n):
    if n == 0:
        return 0
    else:
        return 2 * hanoi(n-1) + 1
