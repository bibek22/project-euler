#!/usr/bin/python

import time
import primeMod as pm
start = time.time()
result = []
for each in pm.getPermut(1023456789):
    nu = str(each)
    if len(nu) < 10:
        continue
    one = (int(nu[1]+nu[2]+nu[3]) % 2 == 0)
    tw = (int(nu[2]+nu[3]+nu[4]) % 3 == 0)
    th = (int(nu[3]+nu[4]+nu[5]) % 5 == 0)
    fo = (int(nu[4]+nu[5]+nu[6]) % 7 == 0)
    fi = (int(nu[5]+nu[6]+nu[7]) % 11 == 0)
    si = (int(nu[6]+nu[7]+nu[8]) % 13 == 0)
    se = (int(nu[7]+nu[8]+nu[9]) % 17 == 0)

    if one and tw and th and fo and fi and si and se:
        print(int(nu))
        result.append(int(nu))

print("So, the sum is ", sum(result))
print("\n---------", time.time()-start, "s ---------------")
