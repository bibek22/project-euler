#!/usr/bin/python

import itertools as it

number = "0123456789"

everyPossible = list(it.permutations(number))

def getint(list, i, j):
    return int("".join(list[i:j]))

sum = 0
for each in everyPossible:
    if (getint(each, 1, 4) % 2 == 0) and (getint(each, 2, 5) % 3 == 0) and (getint(each, 3, 6) % 5 == 0) and (getint(each, 4, 7) % 7 == 0) and (getint(each, 5, 8) % 11 == 0) and (getint(each, 6, 9) % 13 == 0) and (getint(each, 7, 10) % 17 == 0):
        sum += getint(each, 0, 10)

print("so, the sum is :", sum)
