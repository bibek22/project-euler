n=100
sum= n*(n+1)/2
square_sum=0
for x in range(1,101): #needs generalization.
    square_sum+= x**2

required= sum*sum -square_sum 
print required