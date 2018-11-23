n = 20
archive = {}


def choice(x, y):
    global archive
    if (x, y) in archive:
        return archive[(x, y)]
    else:
        if x == 0 or y == 0:
            return 1
        else:
            tmp = choice(x-1, y) + choice(x, y-1)
            archive[(x, y)] = tmp
            return tmp
print choice(20, 20)
print archive
