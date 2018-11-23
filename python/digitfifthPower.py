#!/usr/bin/env python3
import math
import time
start = time.time()


def fifth_power(n=0):
    # returns array of fifth_power of digits.
    result = []
    if n == 0:
        for each in range(10):
            result.append(each**5)
        return result
    else:
        return n**5


power = fifth_power()


def getFifthsum(n):
    num = str(n)
    sum = 0
    round = 1
    for i in num:
        sum += power[int(i)]  # power is a array containing number equal to fifth power of  index 
        if sum > n:
            '''
            sum is over the number already, dont increment it. instead, inrease the digit to the left of the one that topped the sum.
            like if we're checking 135
            1**5 + 3**5 = 243 is already over 135 so, instead of checking 136, incease the digit 3.  drop() function below used to do that. 
            '''
            break
        round += 1
    if sum == n:  # found one of the numbers
        return -2
    elif sum < n:  # still increment the rightmost digit coz sum is not over the number
        return -1
    else:
        return len(num)-round 


def drop(currentNum, place):
    '''
    place counted from the right hand side of number
    so in number 134:
              1     3    4
             2nd    1st  0th <-- place
    '''

    length = len(str(currentNum))   # in above example number: length = 3
    sigfig = 10**(place+1)      #  sigfig = 10** (1+1) = 100 
    num =(math.floor(currentNum / sigfig) + 1) * sigfig   # num = (1 +1) * 100 = 200
    return num  # so start checking from there now.

def main():
    currentNum = 9
    done = False
    summ = 0   # of all the number found which is what we need.
    while not done:
        if currentNum > 1000000:  # largest estimate of the number with the required property.
            done = True
        result = getFifthsum(currentNum)
        if result == -2:
            print("found this: ", currentNum)
            summ += currentNum
        elif result >=0:
            # print("From ", currentNum, "to :", end=" ")
            currentNum = drop(currentNum, result)
            continue
        currentNum += 1
    print("So, the sum is ", summ)
    print("***************************")

if __name__  =="__main__":
    main()
    print("took ", time.time()-start, "secs")
