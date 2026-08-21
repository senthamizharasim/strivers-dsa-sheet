def rever(arr:list,left:int,right:int)->None:
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    rever(arr,left+1,right-1)
nums=[1,2,3,4,5]
rever(nums,0,len(nums)-1)
print(nums)