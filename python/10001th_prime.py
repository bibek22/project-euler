#!/usr/bin/python2
primes = [2, 3]


def nextPrime():
    global primes
    n = primes[-1]
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


def main():
    for i in range(10000):
        nextPrime()
        if i == 9998:
            print primes
            print primes[-1]

main()
