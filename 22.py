import string
from collections import OrderedDict
words_bag = OrderedDict()



file = open('22','r')
filehandler = file.readline()
names = filehandler.split('"')
for name in names:
    if name == '' or ',':
        names.remove(name)



words = sorted(names)

alphabets = tuple(string.ascii_uppercase)


for word in words:
    letters = list(word)
    multiply = 0
    for letter in letters:
        alphabet_value = alphabets.index(letter)+1
        multiply += alphabet_value

    words_bag[word] = multiply*(words.index(word)+1)

print(words_bag)

print(sum(words_bag.values()))







