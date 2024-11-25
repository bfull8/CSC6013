def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
