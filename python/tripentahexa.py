#!/usr/bin/env python3
from math import sqrt
tribase = 0
def tri(n):
    # returns true if n is triangular number T(p), reports p as tribase.
    global tribase
    a = 1
    b = 1
    c = -2*n
    m = (-b + sqrt(b**2 - 4*a*c))/2*a
    d = m if m > 0 else (-b - sqrt(b**2 - 4*a*c))/2*a
    if d % 1 == 0:
        tribase = d
        return True
    else:
        return False

def pent(n):
    global pentabase
    # similar to tri above
    a = 3
    b = -1
    c = -2*n
    m = (-b + sqrt(b**2 - 4*a*c))/2*a
    d = m if m > 0 else (-b - sqrt(b**2 - 4*a*c))/2*a
    if d % 1 == 0:
        pentabase = d
        return True
    else:
        return False

def hex(n):
    # gives nth hex number
    return int((2*n**2 - n))

n = 534
if __name__ == "__main__":
    while True:
        m = hex(n)
        if tri(m) and pent(m):
            found = True
            print(tribase, pentabase, n, (tribase**2 + tribase)/2)
            break
        n += 1
