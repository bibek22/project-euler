#!/usr/bin/python
possible = []
summ = [] 


def hasDouble(n):
    num = str(n)
    if num.count("0"):
        return True
    for each in num:
        if num.count(each) >= 2:
            return True
        else:
            continue
    return False


def check():
    for i in ["123", "12223", "22212", "55555", "22"]:
        print(i, ": ", hasDouble(i))


def isPandigital(n):
    num = str(n)
    if len(num) != 9:
        return False
    else:
        return not hasDouble(num)


for each in range(5000):
    if not hasDouble(each):
        possible.append(each)
# print(possible)
# quit
# i
def main():
    global summ;
    itera = 0
    for each in possible:
        base = each
        for another in possible:
            product = base * another
            itera += 1
            megaNum = str(product) + str(base) + str(another)
            if isPandigital(megaNum):
                print(base, another, "and", product)
                summ.append(product)
    print("so, the sum is ", sum(set(summ)))

if __name__ == "__main__":
    main()
