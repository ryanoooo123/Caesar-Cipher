#this is a Caesar Cipher dencoder and decoder just for practice
import string


lowercaselist = list(string.ascii_lowercase)
uppercaselist = list(string.ascii_uppercase)

context = input('insert your context: ')
shift = int(input('insert shift: '))
final = []
context = list(context)


for i in context:
    new = ''
    if i.islower():
        index = lowercaselist.index(i)
        new = lowercaselist[(index + shift)%26]

    elif i.isupper():
        index = uppercaselist.index(i)
        new = uppercaselist[(index + shift)%26]


    else:
        new = i

    final.append(new)

print(*final, sep='')
    