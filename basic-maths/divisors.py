import math
def divisors(n:int)->list:
    small,large=[],[]
    for i in range(1,math.isqrt(n)+1):
        if n%i==0:
            small.append(i)
            if i!=n//i:
                large.append(n//i)
    divisors=small+large[::-1]
    return divisors
print(divisors(36))