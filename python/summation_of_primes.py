import numpy
primes = [2, 3]
primitive_prime = {}


def primes_primitive(n):
    # primes less than n
    number = numpy.empty(n)  # empty list of size n
    number.fill(1)  # filled with 1/ True
    number[0] = 2
    for each in range(1, len(number)):
        if bool(number[each]):  # if it's value is 1 and not 0.
            key = (2*each+1)
            number[each] = key
            add = key
            key += key
            while key/2 < len(number):
                if not key % 2 == 0:
                    number[(key-1)/2] = 0
                key += add

    return filter(lambda a: a != 0, number)


def nextPrime():
    global primes
    n = primes[-1]
    found = False
    test = n+2
    while not found:
        for prime in primes[1:]:
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


if __name__ == "__main__":
    pass

# while primes[-1] < 1000:
#     nextPrime()
# sum = 0
# for each in primes:
#     sum += each

# print (sum-primes[-1])
# print primes
