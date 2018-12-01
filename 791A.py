s = str(input(''))

l = s.split(' ')

Limark = int(l[0])
Bob = int(l[1])

c = 1
while(True):
    Limark = Limark * 3
    Bob = Bob * 2
    if Limark > Bob:
        break
    else:
        c = c + 1

print(c,end='')
