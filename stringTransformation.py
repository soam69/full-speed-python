def getStr(s):
    k = ""
    for i in range(len(s)):
        k += 3 * s[i]
    return [k,len(k)]

print (getStr("mohan"))

#Thing to learn here was

z = "123"
z = [z[:1] + z[1] + z[1:]]      #This will take elements till z[1] (excluding z[1]) + z[1]  + elements after z[1] (including z[1])
print (z)