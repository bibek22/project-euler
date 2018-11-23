#!/usr/bin/env python3
largest = 0
for i in range(90,100):
    for j in range(90,100):
        amount = sum(list(map(int, list(str(i**j)))))
        if largest < amount:
            largest = amount
print(largest)

# print(max([sum(list(map(int, list(str(i**j))))) for i in range(100) for j in range(100)]))
