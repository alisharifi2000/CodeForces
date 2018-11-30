s1 = str(input(''))
s2 = str(input(''))

s1 = s1.lower()
s2 = s2.lower()

list = []
list.insert(len(list),s1)
list.insert(len(list),s2)

list1 = sorted(list)

if list[0] == list[1]:
    print(0, end="")
elif list[0] == list1[0] and list[1] == list1[1]:
    print(-1, end="")
elif list[0] == list1[1] and list[1] == list1[0]:
    print(1, end="")

