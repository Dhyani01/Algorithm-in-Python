# Program For Binary Search 
# Best Time complexity O(1)
# Average and Worst O(logn)

#Sorted as Prerequisite

Array=[6, 7, 9, 13, 21, 45, 101, 102]


A=int(input("Enter the Number to be searched in the array: "))

i=0
j=len(Array)-1


def Binary_Search(Array,A,i,j):
    mid=int((i+j)/2)
    if Array[mid]==A:
        a=mid+1
        return a
    else:
        if Array[mid]>A:
            return Binary_Search(Array,A,i,mid-1)
        elif Array[mid]<A:
            return Binary_Search(Array,A,mid+1,j)


print(Binary_Search(Array,A,i,j))