A=[4,3,5,1,7,8,9,0]


for i in range(len(A)):
    temp=i
    for j in range(i+1,len(A)):
        if A[j]<A[temp]:
            temp=j
    A[i],A[temp]=A[temp],A[i]
print(A)
