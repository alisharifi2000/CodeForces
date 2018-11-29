string = str(input(''))

string = string.lower()

vowels = ('a', 'e', 'i', 'o', 'u', 'y')

for x in string:
    if x in vowels:
       string = string.replace(x, "")

answer = ""
for items in string:
        answer = answer + "." + items

print(answer)


