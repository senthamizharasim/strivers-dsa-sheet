def onetoN(current:int,n:int)->None:
    if current>n:
        return
    print(current)
    onetoN(current+1,n)
onetoN(4,7)