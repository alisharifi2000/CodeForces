s = str(input(''))
size = len(s)
list = []
if size > 1:
    l = s.split('+')
    for items in l:
        n = int(items)
        list.insert(len(list), n)
    list = sorted(list)
    s2 = ''
    si = len(list)
    for i in range(0, si):
        if not (i == si - 1):
            s2 = s2 + str(list[i]) + '+'
        else:
            s2 = s2 + str(list[i])

    print(s2, end='')

else:
    print(s, end='')
