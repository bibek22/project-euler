#!/usr/bin/env python3

import time
now = time.time()
total = 0
iters = 0
for base in range(1, 10):
    power = 1
    num = base ** power
    while len(str(num)) == power:
        total += 1
        iters += 1
        power += 1
        num = base ** power

print(total, iters)
print(time.time() - now, "s" )
