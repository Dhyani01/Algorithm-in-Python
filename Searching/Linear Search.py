# Program For Linear Search 
# Best Time complexity O(1)
# Average and Worst O(n)



Array=[2143,35452,2,14,5,62,1,14,4,0,7,3]


temp=int(input("Enter the variable to search in the array: "))

flag=0
for i in range(len(Array)):
    if temp==Array[i]:
        flag=1
        break

if flag==1:
    print("Index found at location "+str(i+1))
else:
    print("Element not found")