def ispalin(n):
    new=str(n)
    cond=True
    for x in range(0,(len(new)/2)):
        cond= cond and bool(new[x]== new[-1-x])
    return cond

plausible=[]
for x in range(900, 1000):
    test= str(x)
    if test[-1] in ('3','9'):
        plausible.append(x)
answer=0
for each in plausible:
    for all in plausible:
        if ispalin(each*all):
            answer =each*all
print answer
