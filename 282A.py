n = int(input(''))

c = 0
list = []
for i in range(0,n):
    s = str(input(''))
    l = s.split("X")

    for items in l:
        if(items != ''):
            if(items == '++'):
                c = c + 1
            elif(items == '--'):
                c = c - 1

print(c,end=" ")
