n = int(input(''))
s = str(input(''))
l = s.split(" ")

list = []

for items in l:
    soldier = int(items)
    list.insert(len(list),soldier)

Max = max(list)
Min = min(list)

index_min = []
index_max = []

if Max != Min:
    for i in range(0,len(list)):
        if list[i] == Max:
            index_max.insert(len(index_max),i)
        elif list[i] == Min:
            index_min.insert(len(index_min), i)
    n_swap = 0

    swap_max = min(index_max)
    swap_min = max(index_min)

    if swap_min < swap_max:
        n_swap = len(list) - 1 - swap_min + swap_max - 1
    elif swap_min > swap_max:
        n_swap = len(list) - 1 - swap_min + swap_max
else:
    n_swap = 0

print(n_swap)
