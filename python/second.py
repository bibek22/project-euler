def fib(n):
    second=1
    first=1
    if n in (1,2):
        return 1
    elif n==0:
        return 0
    else:
        for x in range(n-2):
            new= first+second
            first=second
            second=new
        return new

limit=4000000
n=0
sum=0
result=0
while result<limit:
    result=fib(n)
    if result%2==0:
        sum+=fib(n)
    n+=1
print sum