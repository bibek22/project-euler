#!/usr/bin/python

import primeMod as pm
import time
start = time.time()


def shuffle(n):
    result = []
    n = str(n)
    for i in range(1, len(n)):
        result.append(int(n[i:]+n[:i]))
    return result


def has_even(n):
    for each in str(n):
        if int(n) % 2 == 0:
            return True
    return False

many = 1
primes = pm.seive(1000000)
passed = [2]
for each in primes:
    if each in passed:
        many += 1
        print(each)
        continue
    if has_even(each):
        continue
    circles = shuffle(each)
    state = True
    for form in circles:
        if form not in primes:
            state = False
            break
    if state:
        for i in circles:
            passed.append(i)
        many += 1
        print(each)

print("So, there are ", many, "circular primes below a million.")
print("\n--------", time.time()-start, "sec -------------")
