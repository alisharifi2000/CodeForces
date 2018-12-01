s = str(input(''))

l = s.split(' ')

n = int(l[0])
k = int(l[1])

for i in range(1,k+1):
    if n%10 == 0:
        n = int(n/10)
    elif n%10 != 0:
        n = n - 1
        
print(n,end='')
