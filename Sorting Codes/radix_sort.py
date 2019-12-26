def radixsort( aList ):
  RADIX_count = 10
  maxLength = False
  tmp , placement = -1, 1
 
  while not maxLength:
    maxLength = True
    
    buckets = [list() for _ in range( RADIX_count )]
 
    for  i in aList:
      tmp = int(i / placement)
      buckets[tmp % RADIX_count].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 

    a = 0
    for b in range( RADIX_count ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
 
    placement *= RADIX_count
    
count = int(input(" Enter how many elements you want to enter for sorting : "))
sort_list = []
for i in range(count):
    sort_list.append(int(input("Enter No: ")))

radixsort(sort_list)

print(sort_list)
