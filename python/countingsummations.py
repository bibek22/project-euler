#!/usr/bin/env python3
upto = 500
import sys
mil = 1000000
sys.setrecursionlimit(100000)

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def ways(sum, ind):
    if ind == 2:
        return 1 + sum // ind

    count = 0

    for i in range(1+sum//ind):
        count += ways(sum-ind*i, ind-1 )
    return count
ways = Memoize(ways)

upto = 4000
next = ways(upto, upto-1)
while next % mil != 0:
    upto -= 1
    next = ways(upto, upto-1)
    print("doing: ", upto)
print(upto)

# ways_memo = {}
# def ways(sum, ind):
#     if ind == 2:
#         thing = 1 + sum // ind
#         ways_memo[(sum, ind)] = thing
#         return thing

#     count = 0

#     for i in range(1+sum//ind):
#         if (sum-ind*i, ind-1) not in ways_memo:
#             thing = ways(sum-ind*i, ind-1 )
#             ways_memo[(sum, ind)] = thing
#         count += ways_memo[(sum-ind*i, ind-1)]
#     return count
