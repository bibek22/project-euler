#!usr/bin/python
##couldn't be more efficient
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
req_prime={}
def entry(x, dict):
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1


def hPrime(n):
    i=0
    found=False
    temp_prime={}
    while not found:
        prime=primes[i]

        while True:
            if n%prime==0:
                n//= prime
                entry(prime,temp_prime)
                if n==1:
                    for each in temp_prime:
                        try:
                            condn=bool(temp_prime[each]>req_prime[each])
                            if condn:
                                req_prime[each]=temp_prime[each]                                
                        except:
                            req_prime[each]=temp_prime[each]

                    return primes[i]
            else:
                break

        if primes[i]==primes[-1]:
            nextPrime()
        i+=1



for x in range(2,21):
    hPrime(x)

print req_prime

target=1

for each in req_prime:
    target*= each**req_prime[each]
    print target



