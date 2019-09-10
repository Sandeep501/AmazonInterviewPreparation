#Find the number

##### Binary Seach #####

def find(n,k):
        pivot=len(n)//2
        if n[pivot]==k:
            return pivot
        elif k>n[pivot]:
            for i in range(pivot+1,len(n)):
                if n[i]==k:
                    return i
        else:
            for j in range(0,pivot):
                if n[j]==k:
                    return j


##### Linear Search #####
def find(n,k):
    target=n[0]
    if target==k:
        return 0
    else:
        for i in range(1,len(n)):
            if n[i]==k:
                return i
                

#### Test Code ####
s=7
arr =[1,2,4,5,6,7,32,45,67,89,90,123] 

print(find(arr,s))
