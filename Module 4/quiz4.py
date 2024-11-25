def fact(n):
    if (n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5.0))

def fibo(n):
    if (n in [1,2]):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(-5))
