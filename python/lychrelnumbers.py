#!/usr/bin/env python3


def ispalin(n):
    n = str(n)
    state = True
    for ind in range(int(len(n)/2) + 1):
        if n[ind] == n[-1-ind]:
            state = True
        else:
            state = False
            break
    return state


def reverse(num):
    return int(str(num)[::-1])


total = 0
for i in range(10, 10000):
    iter = 1
    current = i
    broken = False
    while iter != 50:
        if ispalin(current):
            broken = True
            break
        else:
            current = current + reverse(current)
        iter += 1
    if not broken:
        total += 1
print(total)

