#!/usr/bin/env python3

longest = 0
d = 0
for i in range(10, 1000):
    num = i
    modulo = 1
    prevs = []
    while (modulo % num not in prevs) and (modulo != 0):
          prevs.append(modulo % num)
        modulo = modulo % num * 10

    final = modulo % num
    length = len(prevs) - prevs.index(final)
    if length > longest:
        longest = length
        d = i


print("so, this: ", d, "is the number you want.")
