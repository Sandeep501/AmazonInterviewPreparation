# https://www.hackerrank.com/challenges/apple-and-orange/problem

# Find the description of the Problem Statement in the above link

SamHouseStart=int(input())
SamHouseEnd=int(input())
AppleTreeLocation=int(input())
OrangeTreeLocation=int(input())
Apples=list(map(int,input().split()))
Oranges=list(map(int,input().split()))
AppleCount=0
OrangeCount=0

for i in range(0,len(Apples)):
    Apples[i]+=AppleTreeLocation
for i in range(0,len(Oranges)):
    Oranges[i]+=OrangeTreeLocation

for i in range(0,len(Apples)):
    if Apples[i]>=SamHouseStart and Apples[i]<=SamHouseEnd:
        AppleCount+=1
        
for i in range(0,len(Oranges)):
    if Oranges[i]<=SamHouseEnd and Oranges[i]>=SamHouseStart:
        OrangeCount+=1
print(AppleCount,"\n",OrangeCount)
