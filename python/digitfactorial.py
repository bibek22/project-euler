#!/usr/bin/env python3


def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


def digitFact(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    return sum

sum = 0
for i in range(10, 2540160):
    if digitFact(i) == i:
        sum += i

print(sum)
