"""There are two sorted array and we want their intersection 
    minimum time to do that is O(m+n)
    where m,n are size of array"""


a=[0,1,2,3,5,6,89,900,100]
b=[0,2,3,4,5,8,9]
m=len(a)
n=len(b)

for i in range(max(m,n)):
    if a[i]==b[i]:
        print(a[i])
    if a[i]>b[i]:
        try :
            if a[i]==b[i+1]:
                print(a[i])
        