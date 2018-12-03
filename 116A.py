n = int(input(''))

list =[0]

exist = 0

for i in range(0,n):
    if exist > 0:
        list.insert(len(list),exist)
    s = str(input(''))

    l = s.split(' ')
    enter = int(l[1])
    exit = int(l[0])

    exist = exist + enter - exit

m = max(list)

print(m)
