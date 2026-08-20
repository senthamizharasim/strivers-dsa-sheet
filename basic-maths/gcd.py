def gcd_brute(a:int,b:int)->int:
    ans=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            ans=i
    return ans
def gcd_euc(a:int,b:int)->int:
    while b:
        a,b=b,a%b
    return a
print(gcd_euc(24,30))
print(gcd_brute(24,30))
