#!/usr/bin/python3
import itertools
primes = []


def generate_prime(n):
    global primes
    primes = seive(n)


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


def get_prime_factors(n):
    # gives a dictionary of primes with the time they divide a given number n.
    global primes
    prime_factors = []
    prime = primes[0]
    index = 0
    while prime <= n:
        while n % prime == 0:
            prime_factors.append(str(prime))
            n /= prime
        index += 1
        prime = primes[index]
    return prime_factors


def factors_sum(n):
    list = get_prime_factors(n)
    sum = 0
    for r in range(len(list)):
        for each in set(itertools.combinations(list, r)):
            devisor = 1
            for bit in each:
                devisor *= int(bit)
            sum += devisor
    return sum

if __name__ == "__main__":
    generate_prime(30000)
    abundant = []
    total = 0
    for number in range(28123):
        found = False
        if number < factors_sum(number):
            abundant.append(number)
        for each in abundant:
            if number - each in abundant:
                found = True
                break
        if not found:
            total += number
            print("adding", number)
    print("Sum: ", total)
