def isSorted(list):
  for i in range(len(list) - 1):
    if (list[i] > list[i+1]):
      return False
  return True

l1 = [1,2,3,4,5]
l2 = [2,5,1,7,3]

print (isSorted(l1))
print (isSorted(l2))