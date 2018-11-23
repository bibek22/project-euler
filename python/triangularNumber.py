#!/usr/bin/python2


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


def nextPrime():
    global primes
    found = False
    test = primes[-1] + 2
    while not found:
        for prime in primes:
            divides = bool(test % prime == 0)
            broken = False
            if divides:
                broken = True
                break
        if not broken:
            primes.append(test)
            break
        else:
            test += 2


def get_factors(n):
    # gives a dictionary of primes with the time they divide a given number n.
    global primes
    prime_factors = {}
    prime = primes[0]
    index = 0
    while prime <= n:
        while n % prime == 0:
            if prime in prime_factors:
                prime_factors[prime] += 1
            else:
                prime_factors[prime] = 1
            n /= prime
        index += 1
        prime = primes[index]
    return prime_factors


def factors_count(n):
    dict_factor = get_factors(n)
    count = 1
    for each in dict_factor:
        count *= dict_factor[each]+1
    return count

limit = 100000
# primes = [2, 3]
# while primes[-1] < limit:
#     nextPrime()
primes = seive(100000)
print "done generating primes"

n = 1
last_triangular = 1
while factors_count(last_triangular) < 500:
    n += 1
    last_triangular += n  # give next triangular number 
print n , "th triangular " , last_triangular
