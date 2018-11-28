w = 5
h = 5
matrix = [[0 for x in range(w)] for y in range(h)]
l = []
for i in range(0,5):
    raw = str(input(''))
    raw = raw.split(' ')
    counter = 0
    for items in raw:
        if int(items) == 1:
            l.insert(len(l),i)
            l.insert(len(l),counter)
        matrix[i][counter] = int(items)
        counter = counter+1

step = abs(l[0]-2)+abs(l[1]-2)
print(step,end='')
