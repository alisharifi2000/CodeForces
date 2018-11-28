import math
in_put = int(input(''))

list = []

in_put1 = str(input(''))
in_put1 = in_put1.split(' ')
for items in in_put1:
    list.insert(len(list),float(items))

Sum = 0.0
for items in list:
    Sum = items + Sum

quater = math.ceil(Sum/2)

counter  = 1
sum = 0

for items in list:
    sum = items + sum
    if(quater<=sum):
        print(counter,end = '')
        break
    else:
        counter = counter+1
