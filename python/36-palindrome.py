#!/usr/bin/python
import primeMod as pm
import time

sum = 0
start = time.time()
number = 1

while number < 1000000:
    if pm.ispalin(number):
        binn = str(bin(number))[2:]
        if pm.ispalin(binn):
            sum += number
    number += 1

print("The sum is ", sum)
print("\n----------", time.time()-start, "secs -------------")
