'''
Example 1:
Input:
5 ---> Value of T
[7,0,5,1,3] ---> E[], element of E[0] to E[N-1], where input each element is separated by new line
[1,2,1,3,4] -----> L[],element of L[0] to L[N-1], where input each element is separated by new line
Output:
8 -----> Maximum number of guests on cruise at an instance.
Explanation:
1
st hour
Entry: 7, Exit: 1
No. of guests on the ship: 6
2
nd hour:
1
st hour
Entry: 0, Exit: 2
No. of guests on the ship: 6 -2 = 4
Hour 3:
Entry: 5, Exit: 1
No. of guests on the ship: 4 + 5 -1 = 8
Hour 4:
Entry: 1, Exit: 3
No. of guests on the ship: 8 + 1 - 3 = 6
Hour 5:
Entry: 3, Exit: 4
No. of guests on the ship: 6 + 3 - 4 = 5
Hence, Maximum Number of guests within 5 hours is 8.
'''
l=[7,0,5,1,3]
k=[1,2,1,3,4]
max=0
sum1=0
for i in range(len(l)):
  sum1 += l[i] - k[i]
  if (max<sum1):
    max=sum1
print(max)
