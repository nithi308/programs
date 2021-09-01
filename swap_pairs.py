'''
O/P: [2, 1, 4, 3, 6, 5, 7]
'''


l=[1,2,3,4,5,6,7]
k=len(l)
if k%2==0:
    pass
else:
    k=k-1
for i in range(0,k,2):
    l[i],l[i+1]  =  l[i+1],l[i]
print(l)
