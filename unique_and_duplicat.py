a = list(x for x in input())
b = list(x for x in input())

s = a + b
d = {}
for i in s:
    d[i] = 0
for i in s:
    d[i] += 1

unique = [x for x in d.keys() if d[x] == 1 ]
dup = [x for x in d.keys() if d[x] > 1 ]


print(unique)
print(dup)
