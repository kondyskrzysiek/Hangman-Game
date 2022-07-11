# a,k,r,i,n,l,s,w,u,o,b 

file = open('slowa.txt', 'r', encoding='utf-8')

lista = [x.strip() for x in file.readlines() if len(x.strip()) == len('osoba')]


dictionary = {}

for i in lista:
    for letter in i:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))  # 28631

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))
"""
max : 'a'

['a : 13187', 'o : 10012', 'i : 9041', 'e : 7998', 'k : 7320', 'u : 7074', 'r : 6892',
 'm : 5877', 'n : 5604', 's : 5580', 'l : 5528', 'y : 5450', 't : 5101', 'p : 4514',
  'w : 4465', 'z : 4390', 'c : 4203', 'd : 3982', 'b : 3416', 'ą : 3341', 'ł : 3085', 
 'g : 2914', 'ę : 2901', 'j : 2841', 'ż : 1887', 'f : 1605', 'h : 1398', 'ó : 1252', 
 'ć : 806', 'ś : 628', 'ń : 509', 'ź : 294', 'x : 51', 'v : 9']
"""


help_lista = []

for word in lista:
    if 'a' == word[4]:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))  # 3272

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'k'

['a : 4249', 'k : 997', 'r : 792', 'i : 752', 'o : 718', 'n : 656', 's : 652', 'u : 601',
 'l : 600', 't : 593', 'p : 509', 'w : 457', 'e : 455', 'm : 455', 'c : 445', 'z : 438',
  'd : 427', 'g : 388', 'b : 382', 'ł : 382', 'y : 299', 'j : 245', 'f : 206', 'ż : 172',
   'h : 171', 'ę : 90', 'ą : 79', 'ó : 51', 'ś : 38', 'ć : 24', 'ź : 18', 'ń : 17', 'v : 1', 'x : 1']

"""

help_lista = []

for word in lista:
    if not 'k' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #2337

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'r'

['a : 3068', 'r : 616', 'i : 587', 'n : 546', 'o : 524', 'l : 459', 't : 455', 's : 450', 'u : 421',
 'p : 392', 'z : 378', 'm : 364', 'c : 362', 'd : 360', 'w : 355', 'g : 352', 'e : 349', 'b : 292',
  'ł : 285', 'y : 218', 'j : 190', 'f : 152', 'h : 150', 'ż : 150', 'ę : 63', 'ą : 60', 'ś : 28',
   'ó : 25', 'ź : 14', 'ć : 9', 'ń : 9', 'v : 1', 'x : 1']
"""

help_lista = []

for word in lista:
    if not 'r' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #1730

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'i'

['a : 2261', 'i : 508', 'n : 468', 'l : 414', 'o : 400', 's : 375', 't : 344', 'p : 320', 'z : 316',
 'u : 315', 'c : 303', 'w : 292', 'm : 284', 'd : 262', 'ł : 256', 'g : 248', 'e : 244', 'b : 212',
  'j : 161', 'y : 152', 'h : 124', 'ż : 120', 'f : 105', 'ę : 56', 'ą : 44', 'ś : 22', 'ó : 13',
   'ź : 13', 'ć : 9', 'ń : 8', 'x : 1']
"""

help_lista = []

for word in lista:
    if not 'i' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #1251

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'n'

['a : 1691', 'n : 351', 'o : 336', 'l : 314', 's : 287', 'u : 273', 't : 265', 'z : 254', 'p : 230', 'c : 225',
 'm : 210', 'w : 210', 'ł : 210', 'e : 199', 'd : 195', 'g : 187', 'b : 152', 'y : 135', 'j : 132', 'h : 107',
  'ż : 99', 'f : 68', 'ę : 40', 'ą : 36', 'ź : 13', 'ó : 12', 'ś : 10', 'ć : 8', 'ń : 6']
"""

help_lista = []

for word in lista:
    if not 'n' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #665

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'l'

['a : 1244', 'l : 268', 'o : 241', 's : 239', 't : 221', 'u : 220', 'z : 213', 'p : 189', 'ł : 189', 'c : 181',
 'm : 176', 'w : 171', 'd : 138', 'e : 138', 'b : 134', 'g : 127', 'y : 109', 'j : 103', 'h : 95', 'ż : 75', 'f : 54',
  'ę : 30', 'ą : 28', 'ó : 10', 'ź : 9', 'ś : 7', 'ń : 6', 'ć : 5']
"""


help_lista = []

for word in lista:
    if not 'l' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #23

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 's'


['a : 900', 's : 199', 'z : 187', 'o : 185', 'ł : 179', 't : 175', 'u : 153', 'm : 144', 'w : 138', 'c : 136',
 'p : 129', 'd : 111', 'b : 95', 'j : 92', 'g : 92', 'y : 89', 'e : 76', 'h : 76', 'ż : 66', 'f : 28', 'ę : 24',
  'ą : 20', 'ó : 10', 'ź : 9', 'ć : 5', 'ń : 5', 'ś : 2']
"""

help_lista = []

for word in lista:
    if 's' == word[1]:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #2337

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'w'

['a : 28', 's : 27', 'w : 11', 'u : 11', 'o : 8', 't : 6', 'p : 5', 'ł : 4', 'z : 3', 'y : 3', 'b : 2',
 'm : 1', 'e : 1', 'd : 1', 'j : 1', 'ą : 1', 'c : 1', 'g : 1']
"""

help_lista = []

for word in lista:
    if not 'w' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #13

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'u'

['a : 16', 's : 15', 'u : 6', 't : 5', 'o : 4', 'p : 4', 'ł : 4', 'b : 2', 'z : 2', 'm : 1', 'd : 1', 'j : 1',
 'ą : 1', 'c : 1', 'g : 1', 'y : 1'] 
"""

help_lista = []

for word in lista:
    if not 'u' in word:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #7

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'o'

['a : 10', 's : 9', 'o : 4', 't : 2', 'ł : 2', 'm : 1', 'd : 1', 'b : 1', 'p : 1', 'ą : 1', 'c : 1', 'z : 1', 'y : 1']
"""

help_lista = []

for word in lista:
    if 'o' == word[0] and 'o' == word[2]:
        help_lista.append(word)

lista = help_lista.copy()
dictionary = {}

for word in lista:
    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

print(len(lista))   #1

print(list(map(lambda x: f'{x} : {dictionary[x]}', sorted(
    dictionary, key=dictionary.get, reverse=True))))

"""
max : 'b'

['o : 2', 's : 1', 'b : 1', 'a : 1']
"""


file.close()
