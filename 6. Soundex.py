def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    if s[0] != s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])

def removeZeros(s):
    res=""
    for i in s:
        if i!='0':
            res+=i
    return res

def soundex(word):
    res=""
    res+=word[0]
    for i in word[1:]:
        if i in [*'aeiouhwy']:
            res+='0'
        elif i in [*'bfpv']:
            res+='1'
        elif i in [*'cgjkqsxz']:
            res+='2'
        elif i in [*'dt']:
            res+='3'
        elif i in [*'l']:
            res+='4'
        elif i in [*'mn']:
            res+='5'
        elif i in [*'r']:
            res+='6'
    res=removeConsecutiveDuplicates(res)
    res=removeZeros(res)
    if len(res)<4:
        for i in range(len(res),4):
            res+='0'
    return res[:4]

print(soundex("Bough"))
print(soundex("Bow"))

    
    
    