from math import sqrt

def get_missing_triplet(a,b,c):
    
    if a==0:
        return sqrt(c**2-b**2)
    elif b==0:
        return sqrt(c**2-a**2)
    else:
        return sqrt(a**2+b**2)

triplet=[]
for x in range(1,1000):
    a= x
    for y in range(1,1000):
        b=y
        c=get_missing_triplet(x,y,0)
        if a+b+c==1000:
            triplet.append(a)
            triplet.append(b)
            triplet.append(c)

print triplet
