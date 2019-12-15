

A=[4,3,5,1,7,8,9,0]
temp=A[0]
for i in range(1,len(A)):
    if temp>A[i]:
        temp=A[i]
print(temp)
