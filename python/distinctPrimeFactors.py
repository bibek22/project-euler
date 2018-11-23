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
    return(primess)


def get_factors(n):
    # gives a dictionary of primes with the time they divide a given number n.
    global primes
    prime_factors = {}
    prime = primes[0]
    index = 0
    while prime <= n:
        while n % prime == 0:
            if str(prime) in prime_factors:
                prime_factors[str(prime)] += 1
            else:
                prime_factors[str(prime)] = 1
            n /= prime
        index += 1
        prime = primes[index]
    return prime_factors


primes = seive(100000)
if __name__ == "__main__":
    streak = 0
    last = []
    last2 = {}
    last3 = {}
    checking = 600
    while streak != 2 and checking < 649:
        broken = False
        factors = get_factors(checking)
        if checking % 1024:
            print(factors)
        for factor in factors:
            if (factor in last and factors[str(factor)] == last[str(factor)]) or (factor in last2 and
                    factors[str(factor)] == last[str(factor)]) or (factor in last3 and
                            factors[str(factor)] ==
                            last[str(factor)]):
                        pass
            else:
                broken = True
                streak = 0
                last = {}
                last2 = {}
                last3 = {}
                break
        if broken:
            checking += 1
        else:
            streak += 1
            if streak == 1:
                last2 = factors

            if streak == 2:
                last3 = factors

            checking += 1

print(checking)
