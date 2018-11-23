#!/usr/bin/python


def selfpower(n, m):
    # takes a number n and returns the last m digits of n^n
    result = 1
    for i in range(n):
        result *= n
        check = str(result)
        if len(check) > m:
            check = check[-m:]
            result = int(check)
    return result

sum = 0
for i in range(1, 1001):
    sum += selfpower(i, 11)
print("so the digit is ", sum)
