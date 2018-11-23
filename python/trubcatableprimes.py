#!/usr/bin/python

import time
import primeMod as pm
start = time.time()
primes = pm.seive(1000000)
print("DONE!!")
found = 0
result = []
for prime in primes:
    prime = str(3797)
    for i in range(len(prime)-1):
        print("checking ", prime[i:], "and", prime[:i])
        if int(prime[i:]) in primes:
            try:
                cond = int(prime[:i]) in primes
                if cond:
                    print("found : ", prime)
            except:
                break
        else:
            break
    found = 1
    if found == 11:
        break
    result.append(prime)


print("The sum is ", sum(result))
print("--------", time.time()-start, "---------")
