raw_word = str(input(''))
size = len(raw_word)
list = []
counter = 0
for items in raw_word:
    if counter == 0:
        item = items.upper()
        counter = counter+1
        list.insert(len(list),item)
    else:
        list.insert(len(list),items)
w = ''
for items in list:
    w = w+str(items)
print(w,end='')
