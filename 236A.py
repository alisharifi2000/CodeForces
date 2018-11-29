string = str(input(''))

list = []
c = 0

for items in string:
    if not (items in list):
        list.insert(len(list),items)
        c = c + 1

if c%2 == 0:
    print("CHAT WITH HER!" , end="")
elif c%2 !=0:
    print("IGNORE HIM!" , end="")
