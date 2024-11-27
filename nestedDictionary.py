friends = {
    "Ajay" : {"age" : 20, "roll" : 15 },
    "nikhil" : {"age" : 19, "roll" : 19},
    "shivank" : {"age" : 20, "roll" : 20}
}

print (friends)                                     # Prints the whole nested dictionary
print (friends["Ajay"])                             # Prints the dictionary "Ajay" which is a key in the dictionary "friends".
print (friends["shivank"]["age"])                   # Prints 20 which is the value of the key "age" which is one of the
                                                    # value of the key "shivnak"

for name,data in friends.items():                   # To loop through a nested dictionary
    print ("Info of", name)                         # First loop to get the key which is name and value which is another dict.
    for key,num in data.items():                    # Second loop to get the key of the value1 and its value. 
        print (key, ":", num)                       # Easyyyyyyyyyyyyyyyyyy