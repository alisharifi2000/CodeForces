s1 = str(input(''))
s2 = str(input(''))

lenght = len(s1)

list =[]
for i in range(0,lenght):
    if s1[i] != s2[i]:
        list.insert(len(list),'1')
    else:
        list.insert(len(list),'0')

result = ''
for items in list:
    result = result + items

print(result,end='')
