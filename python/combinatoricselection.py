#!/usr/bin/env python3
import math


def combin(i, j):
    return math.factorial(i)/(math.factorial(j)*math.factorial(i-j))

total = 0
for i in range(10, 100):
    inside = 0
    for j in range(1, i):
        inside += 1
        if combin(i, j) > 1000000:
            total += 1
print(total)
