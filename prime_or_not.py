n=int(input("enter the value"))
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c>2:
        return ("it is not a prime")
    else:
        return ("it is prime")
print(prime(n))

#