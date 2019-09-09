# python program to move all the non-zero elements to the right side

def challenge(nums):
    counter=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[counter]=nums[i]
            counter+=1
            
    for i in range(counter,len(nums)):
        nums[i]=0
    return nums
lis=[1,2,3,4,0,0,7,89,7,80,0,0,2,30,0]
print(challenge(lis))