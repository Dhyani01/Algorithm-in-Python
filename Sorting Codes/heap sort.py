def parent(i):
    return int(i/2)

def left(i):
    return 2 * i

def right(i):
    return left(i) + 1

def maxHeapify(A,i,sz):
    l = left(i)
    r = right(i)
    largest = None
    if l <= sz and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= sz and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp 
        maxHeapify(A,largest,sz)

def heapsort(A):
    heap_size = len(A)
    middle = int(heap_size/2)
    for i in range(middle,0,-1):
        maxHeapify(A,i,heap_size - 1)

    m = heap_size - 1
    for i in range(m,-1,-1): 
        temp = A[0]
        A[0] = A[i]
        A[i] = temp 
        m = m-1 
        maxHeapify(A,0,m)




A = [16,4,10,14,8,7,9,3,2,4,1]

print("Unsorted: ", A)
heapsort(A)
print("Heap Sorted: ", A)