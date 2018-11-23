#!/usr/bin/python

import primeMod as pm


def getPermut(n):
    n = str(n)

    def loop(n, sets):
        result = []
        if len(sets) == 0:
            if len(n) == 1:
                return [n]
            else:
                here = n[:1]
                got = loop(n[1:], sets)
                for each in got:
                    for index in range(len(each)):
                        new = each[:index] + here + each[index:]
                        result.append(new)
        return result
    result = loop(n, [])
    for i in range(len(result)):
        result[i] = int(result[i])
    return result

prime = pm.seive(10000)
primes = []
for each in prime:
    if each > 1000:
        primes.append(each)

for each in primes:
    got_list = getPermut(each)
    possible_list = []
    for perm in got_list:
        if perm != each:
            possible_list.append(perm)
    for another in possible_list:
        middle = (each + another )/2
        if another in primes and middle in primes and middle in possible_list:
            print("one of the set is ", each, another, ".")
