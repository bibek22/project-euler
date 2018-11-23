#!/usr/bin/python
# Does in about 3.5 secs.
# Uses seive of aristo for primes
import primeMod as pm
limit = 1000000
primess = pm.seive(limit)
possible_length = 10000
found = {
    0: 0
}
last_entry = 0

print("length of primes is ", len(primess))
for prime_index in range(len(primess)-1):
    for_this_prime = found[last_entry]
    new_sum = primess[prime_index]
    # first add for already found largest length
    for i in range(1, for_this_prime):
        if prime_index+i < len(primess):
            new_sum += primess[prime_index+i]
    if new_sum > limit:
        break
    # Now add for new length
    for add_index in range(1, possible_length-found[last_entry]):
        if prime_index+add_index+for_this_prime < len(primess) and new_sum < limit:
            if prime_index == 0:
                new_sum += primess[prime_index+add_index+for_this_prime]
            else:
                new_sum += primess[prime_index+add_index+for_this_prime-1]
        else:
            break
        # check if the sum is prime
        if new_sum in primess:
            found[new_sum] = for_this_prime + add_index + 1
            last_entry = new_sum
            print("added **", new_sum, "** with ", found[last_entry])


print(found)
print(last_entry, "is the largest prime below a million that is written\
 as consecutive prime sum with ", found[last_entry], " primes")
