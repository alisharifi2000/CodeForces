import math

in_put = input('')
in_put = in_put.split(' ')
l = int(in_put[0])
r = int(in_put[1])
a = int(in_put[2])

c = 0

if (l > r):
    c = r
    if (a > (l - r)):
        c = c + (l - r)
        a = a - (l-r)
        c = c + math.floor(a / 2)
    elif (a <= (l - r)):
        c = c + a
elif (l < r):
    c = l
    if (a < r - l):
        c = c + a
    elif (a >= r - l):
        c = c + r - l
        a = a - (r - l)
        c = c + math.floor(a / 2)

elif (l == r):
    c = l
    c = c + math.floor(a / 2)


print(c*2, end='')
