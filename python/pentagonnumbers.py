#!/usr/bin/env python3


def pentagon(n):
    return int(3*( n**2 - n)/2)

pentagons = []
found = []
diff = 10000
index = 2
try:
    while True:
        next = pentagon(index)
        index += 1
        pentagons.append(next)
        for each in pentagons[:-1]:
            if next - each in pentagons:
                print(next, each)
                found.append((next, each))
finally:
    for each in found:
        add = sum(each)
        print("sum: ", add)
        while add < pentagons[-1]:
            pentagons.append(pentagon(index))
            index += 1
        if add in pentagons:
            print( each, each[0]-each[1])
