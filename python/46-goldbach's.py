#!/usr/bin/python

import primeMod as pm
import math
import time
start_time = time.time()
primes = pm.seive(10000)
primes = primes[2:]


def is_sqr(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


for each in range(33, 1000000, 2):
    if each not in primes:
        target = False
        for prime in primes:
            diff = each-prime
            if diff > 1:
                if is_sqr(diff/2):
                    target = True
                    break
            else:
                break
        if not target:
            print("found ", each)
            break
print("--------", time.time()-start_time, "...........")
