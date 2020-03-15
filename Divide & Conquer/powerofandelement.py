""" Divide and conq example time complexity O(logn)"""

import math
def Dac(a,n):
    if n==1:
        return a
    else:
        mid=math.floor(n/2)
        b=Dac(a,mid)
        c=b*b
    return c

c=Dac(2,5)
print(c)