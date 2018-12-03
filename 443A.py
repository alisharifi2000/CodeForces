string = str(input(''))

c = 0

if string != '{}':
    string = string.strip('{')
    string = string.strip('}')

    items = string.split(', ')

    list = []

    for item in items:
        if item not in list:
            list.insert(len(list),item)
            c = c + 1

print(c)
