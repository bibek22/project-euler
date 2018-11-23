#!/usr/bin/python

import time
import primeMod as pm
start = time.time()


def fifth_power(n=0):
    # returns dictionary of fifth_power of digits.
    result = []
    if n == 0:
        for each in range(10):
            result.append(each**5)
        return result
    else:
        return n**5


power = fifth_power()



def drop(currentNum, place):
    len = len(str(currentNum))
    sigfig = 10**(len-place) 
    num =(math.floor(currentNum % sigfig) + 1) * sigfig

def main():
    currentNum = 2
    done = False
    summ = 0
    while not done:
        result = getFifthsum(currnetNum)
        if not result:
            print("found this: ", currentNum)
            summ += currentNum
        elif result >0:
            currentNum += drop(currentNum, result)
            break
        currentNum += 2
