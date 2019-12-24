# Binary Search Program 
# Best case O(1)
# Average and Worst case O(logn)
# It is only applied on sorted array 
import math


Array=[2143,35452,2,14,5,62,1,4,0,7,3]
Array.sort()


temp=int(input("Enter the variable to search in the array: "))
l=0
r=len(Array)-1
while l<=r :
    middle=math.floor((l+r)/2)
    if temp==Array[middle]:
        print("Element found at ", Array.index(Array[middle]))
    if Array[middle]>temp:
        r=middle-1
    else:
        l=middle+1


