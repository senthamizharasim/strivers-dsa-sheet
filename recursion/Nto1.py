def Nto1(n:int)->None:
    if n==0:
        return 
    print(n)
    Nto1(n-1)
Nto1(7)