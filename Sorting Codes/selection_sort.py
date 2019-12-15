A=[4,3,5,1,7,8,9,0]
B=[]

for i in range(len(A)):
    p=min(A)
    B.append(p)
    A.remove(p)
print(B)
