''' 
From the @NumFOCUS telethon

title: J for json
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=5911
edited by: @vitalizzare
date: January 01, 2021
'''

json_a = '''
{
    "a": [1, 2, 3],
    "b": [1, 2, 3]
}
'''

json_b = '''
{
    "b": [1, 2, 3],
    "a": [1, 2, 3]
}
'''

from json import loads
print(f'{loads(json_a) == loads(json_b) = }')

# prior to python 3.6

s = {'one', 'two', 'three'}
print(f"{set(['one', 'two', 'three']) = }")

for x in s:
    print(f'{x = }')

print('-'*15)

for x in s:
    print(f'{x = }')

# violation of word order in s
from string import ascii_lowercase
from random import choice
words = {''.join(choice(ascii_lowercase) for _ in range(10)) for _ in range(10_000)}

for w in words:
    s.add(w)
for w in words:
    s.remove(w)

print('-'*15)

for x in s:
    print(f'{x = }')

from collections import OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

print(f'{od1 = }')
print(f'{od2 = }')

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 3, 'b': 2, 'a': 1}

print(f'{d1 = }')
print(f'{d2 = }')

print(f'{od1 == od2 = }')
print(f'{d1 == d2 = }')

print(f'{(loads(json_a, object_hook=OrderedDict) == loads(json_b, object_hook=OrderedDict)) = }')
