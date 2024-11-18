def hasDuplicates(list):
  for i in range(len(list)):
    for j in range(i+1,len(list)):
      if(list[i]==list[j]):
        return True
  return False

l1 = [1,2,3,4,5]
l2 = [1,2,2,4,5]
print(hasDuplicates(l1))
print(hasDuplicates(l2))