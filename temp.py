def evenSquareSum():
  #write code here
  l1 = [x*x for x in range(21) if (x%2 == 0)]
  return sum(l1)