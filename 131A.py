s = str(input())
list = []
flag = 0
result = ''

for items in s:
    list.append(items)


if len(list)>1:
    for i in range(0, len(list)):
        if list[0].islower():
            if list[i].isupper() and i > 0:
                flag = 1
            elif list[i].islower() and i > 0:
                flag = 2
                break
        elif list[0].isupper():
            if list[i].isupper() and i > 0:
                flag = 3
            elif list[i].islower() and i > 0:
                flag = 2
                break

else:
    if list[0].isupper():
        result = list[0].lower()
    elif list[0].islower():
        result = list[0].upper()

if flag == 1:
    for i in range(0,len(list)):
        if i == 0:
            result = list[i].upper()
        else:
            result = result + list[i].lower()

elif flag == 2:
    for i in range(0, len(list)):
        result = result + list[i]

elif flag == 3:
    for i in range(0, len(list)):
        result = result + list[i].lower()

print(result,end='')



