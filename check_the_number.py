number=int(input("enter the value"))

def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
def prime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c = c + 1
    if c > 2:
        return ("it is not a prime")
    else:
        return ("it is prime")

def div_5(n):
    if n%5==0:
        return ("divisble")
    else:
        return ("not divisible")
def sum_n(n):
    return n*(n+1)/2

print(even_odd(number))
print(prime(number))
print(div_5(number))
print(sum_n(number))
