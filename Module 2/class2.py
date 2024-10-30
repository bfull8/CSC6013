def countPositiveElements(A):
    count = 0
    for x in A:
        if x > 0:
            count +=1
    
    return count

from random import random

A = []
for _ in range((10 ** 9)):
    A.append((random()-0.5)*100)

print(f"Positive elements: {countPositiveElements(A)}")


def uniqueElements(A):
    for i in range(0,len(A) - 1):


