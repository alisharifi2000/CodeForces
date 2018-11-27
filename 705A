num = int(input(''))
s = str('I hate it')

if num >= 2:
    for i in range(2, num + 1):
        list = []
        list = s.split(' ')
        size = len(list)
        for j in range(0,size):
            h = str(list[j])
            if(h == 'it'):
                list[j] = 'that'
        q = ''
        for j in range(0,size):
            if not (j == size-1):
               q = q + str(list[j])+' '
            else:
               q = q + str(list[j])
        s = q

        if i % 2 == 0:
            s = s + ' I love it'
        elif i % 2 == 1:
            s = s + ' I hate it'

print(s, end='')
