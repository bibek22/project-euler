#!/usr/bin/python2
from itertools import permutations
         
for i in xrange(7, 0, -1):
    for j in sorted(permutations(range(1, i+1)))[::-1]:
        l = int("".join([str(k) for k in j]))
        done = True
        m = 2
        while done and (m * m <= l):
            if l % m == 0:
                done = False
            m += 1
        if done:
            print l
            quit()


