n = int(input(''))

string = str(input(''))

c_a = 0
c_d = 0

for items in string:
    if items == 'A':
        c_a = c_a + 1
    elif items == 'D':
        c_d = c_d + 1

if c_a > c_d :
    print('Anton',end='')
elif c_a < c_d :
    print('Danik',end='')
else:
    print('Friendship',end='')
