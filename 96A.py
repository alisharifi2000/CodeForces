s = str(input(''))
size = len(s)
s = s+' '
counter = 0
flag = 0
for i in range(0,size):
    if(s[i] == '0'):
        if(s[i+1] == '0'):
            counter = counter +1
        elif s[i+1] == '1':
            counter  = 0
        if (counter >= 6):
            print("YES", end='')
            flag = 1
            break
    elif(s[i] == '1'):
        if(s[i+1] == '1'):
            counter = counter +1
        elif s[i + 1] == '0':
            counter = 0
        if (counter >= 6):
            print("YES", end='')
            flag = 1
            break

if (flag == 0):
    print("NO",end = '')
