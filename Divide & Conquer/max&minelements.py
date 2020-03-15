"""Max and min using divide and conq Time complexity is O(n) for max and min finding """



def divideandconq(array,i,j):
    if i==j:
        max1=array[0]
        min1=array[0]
        return max1,min1
    elif i==j-1:
        if array[0]>array[1]:
            max1=array[0]
            min1=array[1]
            return max1,min1
        else:
            max1=array[1]
            min1=array[0]
            return max1,min1

    else:
        mid=(i+j)/2
        a,b=divideandconq(array,i,mid)
        c,d=divideandconq(array,mid+1,j)
        if a>c:
            p=a
        else:
            p=b
        if b<d:
            q=b
        else:
            q=d
    return p,q


array=[1,124,54,6326,57,4,357,5638,5686,535]
i=0
j=len(array)
a,b=divideandconq(array,i,j)
print(a)
print(b)