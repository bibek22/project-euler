#!/usr/bin/env python3


def get_sum(n):
    dic = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81,]
    sum = 0
    for i in str(n):
        sum += dic[int(i)]
    return sum
total = 0
for i in range(10000000):
    if i%100000 == 0:
        print(i)
    sum = get_sum(i)
    while sum != 1 or sum != 89:
        sum = get_sum(sum)
    if sum == 89:
        total += 1
print(total)
