#!/usr/bin/env python3


def seive(n):
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
    # primess = primess[]
    return(primess)

primes = seive(7654321)
largest = 0
for each in primes:
    if len(str(each)) > len(set(str(each))):
        continue
    else:
        if "9" not in str(each) and "8" not in str(each):
            largest = each

print("so, the largest pandigital prime is ", largest)
