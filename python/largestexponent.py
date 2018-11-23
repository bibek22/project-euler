#!/usr/bin/env python3
from math import log
import time
now = time.time()
handler = open("base-exp.txt", 'r')

largest = 0
next = handler.readline()[:-1].split(',')
line = 1
answer = 0
while len(next) == 2:
    new = int(next[-1]) * log(int(next[0]))
    if new > largest:
        largest = new
        answer = line
    line +=1
    next = handler.readline()[:-1].split(',')

print(answer)
print(time.time() - now)
