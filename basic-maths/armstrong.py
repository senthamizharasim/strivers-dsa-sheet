def count(n:int)->int:
    if n==0:
        return 0
    n=abs(n)
    counts=0
    while n>0:
        n=n//10
        counts+=1
    return counts
def armstrong(n:int)->bool:
    length=count(n)
    original=n
    total=0
    while n>0:
        digit=n%10
        total+=digit**length
        n=n//10
    return original==total
print(armstrong(153))
print(armstrong(12))

        
