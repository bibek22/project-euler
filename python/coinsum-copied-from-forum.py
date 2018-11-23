#!/usr/bin/env python3
from time import time

start = time()

# ignore the 1p, since the number of those coins is determined
# by the number of all the higher-valued coins.

coins = [200, 100, 50, 20, 10, 5, 2]

def recurse(index, remaining):
    if index+1 == len(coins):
        return 1 + remaining//coins[index]
    count = 0
    for i in range(0, 1 + remaining//coins[index]):
        count += recurse(index+1, remaining - i*coins[index])
    return count

print(recurse(0, 200))

print("Time: {0} secs".format(time()-start))
