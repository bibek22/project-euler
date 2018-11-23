#!/usr/bin/python

import time
import primeMod as pm

start = time.time()
done = []
limit = 300
primes = pm.seive(limit)
summ = 0
print(primes)


def amicable(n):
    partial_multiples = [1]
    iterable = [1]
    remain = n
    for each in primes:
        print(each)
        if remain == 1:
            break
        if each > remain:
            each = remain
        if remain % each == 0:
            for multiple in iterable:
                new = multiple * each
                partial_multiples.append(new)
            remain /= each
        iterable = partial_multiples
    return sum(partial_multiples)

for check in range(1, limit):
    if check in primes:
        continue
    got = amicable(check)
    if check == amicable(got):
        done.append(check)
        done.append(got)
        summ += check + got
        print(summ)

'''    if check not in giant:
        probable = amicable(check)
        print(check, "==>", probable)
    else:
        print("found in record ", check)
        probable = giant[check]

    if probable in giant and giant[probable] == check:
        summ += check + probable
    elif amicable(probable) == check:
        summ += check + probable
'''

print("The sum is ", summ, ".")
print("Took : ", time.time() - start, "secs")
