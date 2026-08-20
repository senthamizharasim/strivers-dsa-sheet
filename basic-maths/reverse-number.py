def reverse(n:int)->int:
    sign=-1 if n<0 else 1 
    n=abs(n)
    rev=0
    while n>0:
        last_digit=n%10
        rev=rev*10+last_digit
        n= n//10
    return sign*rev
print(reverse(-31))
