'''
For Example:
Suppose, Arr[] = {7, 6, 8, 6, 1, 1}
{7, 6, 8, 6, 1, 1} - {7, 6, 8, 6, 2}, cost = 2
{7, 6, 8, 6, 2} - {7, 6, 8, 8}, cost = 8
{7, 6, 8, 8} - {13, 8, 8}, cost =13
{13, 8, 8} - {13, 16}, cost = 16
{13, 16} - {29}, cost = 29
2 + 8 + 13 + 16 + 29 = 68
Hence, the minimum cost to assemble all gold wires is : 68
'''
l=[12,2,2,5]
s1=0
count=0
for i in range(len(l)-1):
  l.sort()
  #print(l)
  s1=l[0] + l[1]
  count+=s1
  #print(s1)
  del l[0]
  del l[0]
  l.append(s1)
print(count)
