total = 999999
number = ""


def permutation(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while bool(total-1):
    print "total: ",total
    choices = permutation(len(options)-1)
    print "permutations:", choices
    gone = 0
    while total-choices>=0:
        gone += 1
        total = total - choices
        print gone, ">>", total
    number += str(options[gone])
    print "number", number
    options.remove(options[gone])
    print options
print number
