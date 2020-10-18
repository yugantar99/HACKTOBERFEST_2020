def selection_sort(alist):
  for i in range(0,len(alist)-1):
    smallest_value = i
    for j in range(i+1,len(alist)-1):
      if alist[j] < alist[smallest_value]:
        smallest_value = j
    alist[i], alist[smallest_value] = alist[smallest_value], alist[i]
    
blist = input("Enter the list of numbers: ").split()
blist = [int(x) for x in alist]
selection_sort(blist)
print("Sorted List : ", end="")
print(alist)
