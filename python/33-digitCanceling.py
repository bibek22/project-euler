#!/usr/bin/python
import time
start = time.time()
found = []

def evaluate(i, j, n):
    return (int(str(i)+ str(n))/int(str(j) + str(n)) == i/j) or ( int(str(i)+ str(n))/int(str(n) + str(j)) == i/j) or ( int(str(n)+ str(i))/int(str(n) + str(j)) == i/j) or ( int(str(n)+ str(i))/int(str(j) + str(n)) == i/j)
for i in range(1, 10):
    for j in range(1, 10):
        print(j)
        if i == j:
            continue
        for n in range(1, 10):
            if evaluate(i, j, n):
                print(i, "\t", j,  "\t", n)
                if i/j < 1:
                    found.append((i,j, n))

print(found)
