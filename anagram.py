'''
anagram is the string with same elements but different positions makes a word'''
def anagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if n1 != n2:
       return 0
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(0,n1):
        if str1[i] != str2[i]:
           return 0
    return 1
str1="test"
str2="estt"
print(anagram(str1,str2))

#alternate

def check(x):
    d = {}
    for i in x:
        d[i] = 0
    for i in x:
        d[i] += 1 
    return d
def anagram(a,b):
    if check(a) == check(b):
        print("anagram")
    else:
        print("not")

a = "test"
b = "est t"
anagram(a,b)
