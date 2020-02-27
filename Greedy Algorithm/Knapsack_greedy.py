"""Fractional KnapSack problem includes some n elements that have a weight and cost in it and we have to find maximum profit from it so what we do is
   we find the ratio of the two and sort them in descending order then what we do is take the first element who has heighest ratio completly
  such that before moving on we check our knapsack size and reduce the selected weight from our knapsack and repeat the process till our knapsack size is 0
  and for last element we take remaing ratio of its weight """


"""

     Ratio = Value / weight
     for sorting we gets time complexit O(nlogn)  # if doubt open sorting codes
     and for linear operations O(n)
      
      Time COmplexity Becames T(n) = O(n)+O(nlogn)=> O(nlogn)

"""

""" Items => (value, weight) pairs
  arr[] = {{60, 10}, {100, 20}, {120, 30}}
  Knapsack Capacity W = 50"""
    

items=[[60,10],[100,20],[120,30]]
W=50

list_1=[]
for i in range(len(items)):
    a=items[i][0]/items[i][1]
    list_1.append(a)
list_1.sort(reverse=True)


for i in range(len(items)):
    if 





