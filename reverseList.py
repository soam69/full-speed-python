def reverse(list):
  reversedList = []
  for i in range(len(list)-1,-1,-1):
    reversedList.append(list[i])
  return reversedList

l1 = [1,2,3,4,5]
print(reverse(l1))