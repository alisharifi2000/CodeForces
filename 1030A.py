n = int(input(''))
s = str(input(''))

flag = 0
if n > 1 :
    l = s.split(' ')
    for items in l:
        if items != '0':
            flag = 1 
            break
else:
    if s == '1' :
        flag = 1

if flag == 1:
    print('HARD',end='')
else:
    print('EASY',end='')
