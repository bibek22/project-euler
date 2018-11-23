#!/usr/bin/python

import time
start = time.time()

length = 0
start = 1
record = []
target = 1
while length < 1000100:
    if start < 10:
        length += 1
    elif start < 100:
        length += 2
    elif start < 1000:
        length += 3
    elif start < 10000:
        length += 4
    elif start < 100000:
        length += 5
    elif start < 1000000:
        length += 6
    elif start < 10000000:
        length += 7
    if length >= target:
        record.append((start, length))
        target *= 10
    start += 1
product = 1
for each in record:
    over = each[1] % 10
    number = str(each[0])
    if len(number) == 1:
        digit = int(number[-over])
    else:
        digit = int(number[-1-over])
    print(each, "====>", digit)
    product *= digit

print("The product is ", product, ".")
print("\n---------------", time.time()-start, "sec ---------------")
