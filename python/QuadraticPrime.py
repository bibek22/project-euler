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


def evaluate(n, a, b):
    return ( n**2 + a*n + b )

primes = seive(100000)
# possible = []
sofar = 0
sofarVal = ()
# for a in range(-999, 1000):
#     if a % 128 == 0:
#         print(":: a: ", a)
#     for b in primes[:168]:  # primes below 1000
#         n = 0
#         value = evaluate(n, a, b)
#         while value in primes:
#             n += 1
#             value = evaluate(n, a, b)

#         # if n > 40:
#             # possible.append((a, b))
#         if n > sofar:
#             sofar = n
#             sofarVal = (a, b)

for b in primes[:168]:  # primes below 1000
        if b % 128 == 0:
            print(":: b: ", b)
        for p in primes[:168]:
            a = p - b - 1
            n = 0
            value = evaluate(n, a, b)
            while value in primes:
                n += 1
                value = evaluate(n, a, b)

        # if n > 40:
            # possible.append((a, b))
            if n > sofar:
                sofar = n
                sofarVal = (a, b)



# print("length : ", len(possible))
print('sofar: ', sofar, " consecutive primes with values")
print('(a, b): ', sofarVal)
