A=[4,3,5,1,7,8,9,0]
i=0
j=len(A)-1
def merge(A,i,p,q,j):
    
def merge_sort(a,i,j):
    if i==j:
        return A[0]
    else:
        mid=int((i+j)/2)
        mergesort(A,i,mid)
        mergesort(A,mid+1,j)
        merge(A,i,mid,mid+1,j)

    return A


