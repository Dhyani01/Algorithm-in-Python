a=[0,1,2,3,4,342,1,414,2125,5,112,424,2424,1,124,421,0]

# Works great on O(n^2) and small data sets not good for large data sets
for i in range(1,len(a)):
    for j in range(i-1,-1,-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
