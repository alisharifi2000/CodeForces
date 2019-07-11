def change(string,n):
    change = []
    for i in range(0,n):
        if i+1 <n :
            if string[i] == 'B' and string[i+1] == 'G':
                if i not in change:
                    string[i],string[i+1] = string[i+1],string[i]
                    change.append(i+1)
    return string





s = str(input())
l = s.split(' ')
n = int(l[0])
times = int(l[1])
input_string = str(input())
string = list(input_string)

for i in range(0,times):
    string = change(string,n)

result = ''
for items in string:
    result = result+items

print(result,end='')
