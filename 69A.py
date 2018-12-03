n = int(input(''))

t_x = 0
t_y = 0
t_z = 0

for i in  range(0,n):

    s = str(input(''))
    l = s.split(' ')

    t_x = t_x + int(l[0])
    t_y = t_y + int(l[1])
    t_z = t_z + int(l[2])

if t_x == 0 and t_y == 0 and t_z == 0 :
    print("YES",end='')
else:
    print("NO",end='')
