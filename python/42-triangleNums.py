#!/usr/bin/python

import time
start = time.time()


def trianglenums():
    defined = []
    for each in range(1, 40):
        num = (each**2 + each)/2
        defined.append(int(num))
    return defined

defined = trianglenums()
print(defined)
found = 0
with open("/home/bibek/Downloads/words.txt", "r") as wordstream:
    for line in wordstream:
        for each in line.split(","):
            sum = 0
            for letter in each:
                add = ord(letter) - 64
                if add in range(1, 27):
                    sum += add
            if sum in defined:
                found += 1

print(found, " words match the criteria.")
print("\n-----------", time.time()-start, "sec ---------")
