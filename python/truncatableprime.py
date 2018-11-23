#!/usr/bin/env python3


def seive(n):
    '''returns list of primes below n'''
    nums = [1] * n
    primess = []
    for i in range(len(nums)-2):
        each = i + 2
        if nums[each] == 1:
            primess.append(each)
            multiple = 2
            next = multiple * each
            while next < n:
                nums[next] = 0
                multiple += 1
                next = each * multiple
    return(primess)

primes = seive(800000)   # range optimized after getting the answer :D

total = 0  # found so far
ind = 4    # index of primes currently checking
done = primes[ind]  # the prime being checked
found = []
try:
    while total !=11 and done < primes[-1]:
        ind += 1
        sofar = True
        doneStr = str(done)
        broken = False
        for d in [0, 4, 6, 8]:
            if str(d) in doneStr:
                broken = True
                break
        if not broken:
            for d in [2, 5]:
                if str(d) in doneStr[1:-1]:
                    broken = True
                    break
        if broken:
            done = primes[ind]
            continue
        else:
            for i in range(1, len(doneStr)):
                if not (( done // (10 ** i) in primes ) and ( done % (10 ** i) in primes )):
                    sofar = False
            if sofar:
                found.append(done)
                total += 1
            done = primes[ind]
finally:
    print("\n\n Found this much so far: ", found)
    sum = 0
    for each in found:
        sum += int(each)
    print("Sum : ", sum, "\n")
