string = str(input(''))

cu = 0
cl = 0

for items in string:
    if items.isupper():
        cu = cu + 1
    elif items.islower():
        cl = cl + 1

if cl>=cu:
    string = string.lower()
elif cu>cl:
    string = string.upper()

print(string,end=" ")
