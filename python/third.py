#!usr/bin/python

given=600851475143
primes=[2]
def nextPrime():
    global primes
    n=primes[-1]
    found=False
    test=n+1
    while not found:
        for prime in primes:
            divides= bool(test%prime==0)
            broken=False
            if divides:
                broken=True
                break
                
        if not broken:
            primes.append(test)
            break
        else:
            test+=1

def hPrime(n):
    i=0
    found=False
    while not found:
        while True:
            if n%primes[i]==0:
                n//= primes[i]
                if n==1:
                    return primes[i]
            else:
                break
        if primes[i]==primes[-1]:
            nextPrime()
        i+=1
    

print hPrime(given)
