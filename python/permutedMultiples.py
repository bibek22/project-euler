#!/usr/bin/env python3

found = False
start = 111111
while not found:
    sett = list(str(start))
    sett.sort()
    matched = True
    for i in range(2, 7):
        match = list(str(start*i))
        match.sort()
        if sett == match:
            continue
        else:
            matched = False
            break
    if matched:
        print("found", start)
        found = True

    start += 1
