def palindrome(n:int)->bool:
    if n<0:
        return False
    original=n
    rev=0
    while n>0:
        last_digit=n%10
        rev=rev*10+last_digit
        n=n//10
    return original==rev
print(palindrome(34))
print(palindrome(121))