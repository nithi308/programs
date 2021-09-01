'''

Array: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
1
5
9
13
14
10
6
2
3
7
11
15
16
12
8
4

'''
l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("Array:",l)
row=len(l)
col=len(l[0])
for j in range(col):
  if j % 2==0:
    for i in range(row):
      print(l[i][j])
  else:
    i=row -1 
    while(i>=0):
      print(l[i][j])
      i=i-1
