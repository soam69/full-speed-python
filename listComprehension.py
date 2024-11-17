l1 = [x*x for x in range (1,11)]                                        # does x^2 for the range 1 to 10 and adds them to list
print (l1)

l2 = [x*x for x in range (1,11) if (x%2 == 0)]                          # We can also add a condition if we want.
print (l2)