n = int(input(''))

Mishka_win = 0
Chris_win = 0

for i in range(0,n):
    s = str(input(''))
    line = s.split(' ')
    Mishka_dice = int(line[0])
    Chris_dice = int(line[1])

    if Mishka_dice > Chris_dice:
        Mishka_win += 1
    elif Mishka_dice < Chris_dice:
        Chris_win += 1
  
if Mishka_win > Chris_win:
    print("Mishka",end='')
elif Mishka_win < Chris_win:
    print("Chris",end='')
else :
    print("Friendship is magic!^^",end='')
