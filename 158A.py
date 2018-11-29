s = str(input(''))

inputs = s.split(" ")

n = int(inputs[0])
k = int(inputs[1])

list = []

line = str(input(''))
l = line.split(" ")

for items in l:
    num = int(items)
    list.insert(len(list),num)

check = list[k-1]

c = 0
for i in range(0,n):
    if list[i]>=check and list[i] > 0 :
        c = c+1

print(c,end=" ")


