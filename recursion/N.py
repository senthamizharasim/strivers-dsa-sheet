def print_name(n:int,name:str="Phil"):
    if n==0:
        return 0
    print(name)
    print_name(n-1,name)
print_name(4)