def palindrome(s:str,left:int,right:int)->bool:
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(s,left+1,right-1)
print(palindrome("madam",0,len("madam")-1))