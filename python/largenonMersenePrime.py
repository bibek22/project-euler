#!/usr/bin/env python3

number = 1
power = 7830457

start = 28433

while power >34:
    start *= 17179869184
    power -= 34
    start = int(str(start)[-11:])

start *= 2**power
start = int(str(start)[-10:])
print(start + 1)
