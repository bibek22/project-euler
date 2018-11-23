#!/usr/bin/env python3
import time
now = time.time()
def getConcat(num, n):
    sum = ''
    for i in range(1, n+1):
        sum += str(i*num)
    return sum
found = []
largest = 0
for j in range(5):
    for i in range(918273645 // 10**(9-j), 10**(j)):
        pandigit = getConcat(i, 1)
        n = 2
        while len(pandigit) < 10:
            if len(pandigit) != 9 or len(set(pandigit)) != 9:
                pandigit = getConcat(i, n)
                n += 1
            else:
                if int(pandigit) > largest:
                    if not "0" in pandigit:
                        found.append(int(pandigit))
                        largest = int(pandigit)
                    pandigit = getConcat(i,n)
                    n += 1

print(found)
print("largest: ", largest)
print(time.time() - now, "s.")

