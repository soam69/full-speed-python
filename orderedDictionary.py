# Although dictionaries do not follow any order and change it every time the code runs. 
# There is a way to make ordered dictionaries.
from collections import OrderedDict

prices = OrderedDict()

prices["apple"] = 20
prices["banana"] = 40
prices["oranges"] = 60

for x in prices:
    print (x)                               # Prints all the keys

for x in prices.keys():                     # Prints all the keys
    print (x)

for x in prices:
    print (prices[x])                       # Pritns all the values of the keys

for x in prices.values():
    print(x)                                # Prints all the values of the keys

