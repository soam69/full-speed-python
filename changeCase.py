def changeCase(str):                                        #My Solution
    a = ""
    b = ""
    for i in range(len(str)):
        if (str[i] >= 'A') & (str[i] <= 'Z'):
            a += chr(ord(str[i]) + 32)
        else:
            a += str[i]

    for i in range(len(a)):
        if (str[i] >= 'a') & (str[i] <= 'z'):
            b += chr(ord(str[i]) - 32)
        else:
            b += str[i]
    return [b,a]

def changeTheCase(str):                                     #The ideal Solution
    a = str.upper()
    b = str.lower()
    return [a,b]

print (changeCase("Mohan is Sigma321"))
print (changeTheCase("Mohan is Sigma321"))