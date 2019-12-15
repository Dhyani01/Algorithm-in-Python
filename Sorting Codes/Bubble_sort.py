a=[0,1,2,3,4,342,1,414,2125,5,112,424,2424,1,124,421,0]
for i in range(len(a)-1):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]


print(a)
