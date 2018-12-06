side = str(input(''))

dict_L = {'q': 'w', 'w': 'e', 'e': 'r',
          'r': 't', 't': 'y', 'y': 'u',
          'u': 'i', 'i': 'o', 'j': 'k',
          'o': 'p', 'p': '[', '[': ']',
          'a': 's', 's': 'd', 'd': 'f',
          'f': 'g', 'g': 'h', 'h': 'j',
          'k': 'l', 'l': ';', ';': "'",
          'z': 'x', 'x': 'c', 'c': 'v',
          'v': 'b', 'b': 'n', 'n': 'm',
          'm': ',', ',': '.', '.': '/'}

dict_R = {']': '[', '[': 'p', 'p': 'o',
          'o': 'i', 'i': 'u', 'u': 'y',
          'y': 't', 't': 'r', 'r': 'e',
          'e': 'w', 'w': 'q', '.': ',',
          "'": ';', ';': 'l', 'l': 'k',
          'k': 'j', 'j': 'h', 'h': 'g',
          'g': 'f', 'f': 'd', '/': '.',
          'd': 's', 's': 'a', ',': 'm',
          'm': 'n', 'n': 'b', 'b': 'v',
          'v': 'c', 'c': 'x', 'x': 'z',}

string = str(input(''))

string = string.lower()

result = ''

if side == 'R':
    for items in string:
        result = result + dict_R.__getitem__(items)

else:
    for items in string:
        result = result + dict_L.__getitem__(items)

print(result,end='')

