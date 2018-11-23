total = 1
n = 1
last = 1
while n < 501:
    side = 2 * n
    total += 4 * last + 10 * side
    n += 1
    last += 4 * side
print total
