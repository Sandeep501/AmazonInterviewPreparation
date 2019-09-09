# To find the largest element in the Array
##### 1.Linear Search ######

def maxElement(arr):
    minElement=arr[0]
    for i in range(0,len(arr)):
        if minElement<arr[i]:
            minElement=arr[i]
    return minElement
###### 2.sort and find  ######

def maxElement(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr[-1]

##### Test code ######    
lis=[2,3,5,76,89,5,32,21,678,334,323]
print(maxElement(lis))
