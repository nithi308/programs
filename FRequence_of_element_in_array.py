# Finding the frequency of elements in an array
import collections

arr = [4, 3, 99, 3, 99]

count = collections.defaultdict(int)

for i in res:
  count[i] += 1
  if count[i] == 1:
    print(i, ":", arr.count(i))
    
# nithin's code


# arr = [12, 13, 24, 12, 12, 13]
# dict1 = list(dict.fromkeys(arr))
# for i in dict1:
#     print(f"{i} is repeated {arr.count(i)} time\'s")
