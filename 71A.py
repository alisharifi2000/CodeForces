n = int(input(''))
list = []
for i in range(0,n):
    word = str(input(''))
    size = len(word)
    if size>10 :
       w = ''
       w = w+word[0]
       w = w+str(size-2)
       w = w+word[size-1]
       list.insert(len(list),w)
    else:
       list.insert(len(list), word)

size = len(list)
counter = 0
for items in list:
    if counter == size-1:
        print(items,end ='')
    else:
        print(items)
        counter = counter + 1
