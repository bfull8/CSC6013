import math

#for num in range(1,11):
 #   print(num, ":",round(math.log2(num),4), round(math.log2(num)))

#for num in range(1,11):
 #   print(num, ":",round(math.sqrt(num)))

#for num in range(1,11):
 #   print(num, ":",round(num * math.log2(num)))

#for num in range(1,11):
   # print(num, ":",round(num ** 2))

#for num in range(1,11):
 #   print(num, ":",round(num ** 3))

#for num in range(1,11):
 #   print(num, ":",round(2 ** num))

#for num in range(1,11):
 #   print(num, ":",round(math.factorial(num)))

#total = 0
#for num in range(1,16):
 #   total += num ** 2

#total = 0
#for num in range(11):
 #   total += 2 ** num

total = 0
for num in range(1,9):
    total += 2 ** (-num)

print(round(total,3)
