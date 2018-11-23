#!/usr/bin/python2
import math

def prime_test(n):
	for i in xrange(2, int(math.sqrt(p))+1):
		if n % i == 0: return False
	else: return True

primes = [ p for p in xrange(2, 3937) if prime_test(p) == True ]
	
index = 0
while prime_test(sum(primes)) == False:
    index += 1
    primes = primes[index:]

print '%d is the highest consecutive prime sum.' % sum(primes)

