ll1 = list(i for i in input())

num = int("".join(ll1)) + 1

ll2 = list(i for i in str(num))

for i in range(len(ll2)):
    if len(ll1) != len(ll2):
        print(0)
        break
    elif ll1[i] != ll2[i]:
        print(i + 1)
        break
