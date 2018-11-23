#!/usr/bin/python
import math


def isPan(prime):
    number = str(prime)
    digits = []
    for digit in number:
        if (digit in digits):
            return False
        else:
            digits.append(digit)
    return True

primes = [2, 3]
last_prime = 3


def next_prime():
    global last_prime
    global primes
    while True:
        while True:
            last_prime = last_prime + 2
            for each in primes:
                if last_prime % each == 0:
                    break
            primes.append(last_prime)
            return last_prime


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


def isPrime(n):
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


def isPermutNum(n, m):
    # Returns true if two numbers n and m are permutations of digits in each other
    # and False otherwise.
    n = str(n)
    m = str(m)
    for each in n:
        if each not in m:
            return False
    for each in m:
        if each not in n:
            return False
    return True



def factors(n):
    # returns prime factors of n in dictionary.
    # primes = seive(n+1)
    result = {}
    while n != 1:
        for each in primes:
            if n % each == 0:
                if each in result:
                    result[each] += 1
                else:
                    result[each] = 1
                n /= each

    return result


def is_sqr(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False


def getPermut(n, m=0, result=[]):
    # return list with permutation of digits in number n.
    # With optional argument m, returns combination of digits
    # in n taken m at a time.

    n = str(n)

    def loop(n, sets, m=-1):
        result = []
        if len(n) == 1:
            return [n]
        else:
            here = n[:1]
            got = loop(n[1:], sets, )
            for each in got:
                for index in range(len(each)):
                    new = each[:index] + here + each[index:]
                    result.append(new)
        return result

    if m == -1:
        result = loop(n, [])
    else:
        if len(result) == 0:
            for each in n:
                result.append(each)
        else:
            got = result
            result = []
            for number in got:
                for digit in n:
                    new = number + digit
                    result.append(new)
            if m-1 == 0:
                return result
        return getPermut(n, m-1, result)
    for i in range(len(result)):
        result[i] = int(result[i])
    return result


def ispalin(n):
    n = str(n)
    state = True
    for ind in range(int(len(n)/2) + 1):
        if n[ind] == n[-1-ind]:
            state = True
        else:
            state = False
            break
    return state


def shuffle(n):
    result = []
    n = str(n)
    for i in range(1, len(n)):
        result.append(int(n[i:]+n[:i]))
    return result
