file = open("/content/drive/MyDrive/text.txt", "r")
name = []
age = []
place=[]
for i in file:
    if '\n' in i:
        i = i.replace('\n','')
    l = i.split()

    name.append(l[0])
    age.append(int(l[1]))
    place.append(l[2])
    print(l)

print(name[age.index(max(age))], place[age.index(max(age))])
