def findOccur(str):                                     #My Method of solving the question
    for i in range (len(str)):
        if(str[i] == "b"):
            a = i
            break

    for i in range (len(str)):
        if ((str[i]+str[i+1]+str[i+2]) == "ccc"):
            b = i
            break
    return [a,b]

def findOccurence(s):
    a = s.find("b")
    b = s.find("ccc")
    return [a,b]

print (findOccur("aaabbccc"))
print (findOccurence("aaabbccc"))
