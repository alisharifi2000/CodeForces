string = str(input(''))

list = []

for items in string:
    if items == 'h' or items == 'o' or items == 'l' or items == 'e':
        list.insert(len(list),items)

c_h = 0 #flag for h
c_e = 0 #flag for e
c_l = 0 #counter for h
c_o = 0 #flag for o

result = ''

for items in list:
    if items == 'h' and c_h == 0:
        c_h = 1
        result = result + items
    if items == 'e' and c_e == 0 and c_h == 1:
        c_e = 1
        result = result + items
    if items == 'l' and c_e == 1 and c_l < 2:
        c_l = c_l + 1
        result = result + items
    if items == 'o' and c_l == 2 and c_o == 0:
        c_o = 1
        result = result + items


if result == 'hello':
    print('YES',end='')

else:
    print('NO',end='')
