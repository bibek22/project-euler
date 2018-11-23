last = 1
sec_last = 0
index = 2

def fib():
    #  returns next fibonacci number as string every time.
    global last
    global index
    global sec_last
    index += 1
    new = last + sec_last
    sec_last = last
    last = new
    return str(new)

while len(fib()) < 10000:
    pass
print index
print sec_last
