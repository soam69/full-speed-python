friends = {                 # Dictionary is basically a data structres with keys & values
    "ajay" : 15,            # Instead of using traditional index values (0,1,2...), it uses specific keys to access specific element
    "faiza" : 16,           # It is not in ascending order
    "nikhil" : 19,
    "shivank" : 20,
    "soham" : 23,
    "tanishka" : 37,
}

print(friends)                      # prints the whole dictionary
print(friends["ajay"])              # prints the roll number of specific key. (ajay in this case)
for key,value in friends.items():    # friends.items() is basically returns one item at a time i guess
    print (key,value)

# To make a empty dictionary
fruits = dict() # or enemies = {}
# To add items to a dictionary
fruits["apple"] = 20
fruits["banana"] = 40
print (fruits)                          # The order in which elements are inserted is not maintained. It changes everytime code runs


