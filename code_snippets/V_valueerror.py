''' 
From the @NumFOCUS telethon

title: V for ValueError
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=14221
edited by: @vitalizzare
date: January 15, 2021
'''

def mean(xs):
    if not xs:
        raise ValueError('Empty sequence is not allowed')
    return sum(xs)/len(xs)

print(f'{mean([1,2,3]) = }')
try:
    print(f'{mean([]) = }')
except ValueError as e:
    print(repr(e))

# KeyError

d = {
    'a': 1,
    'b': 2,
    }

try:
    print(f"{d['c'] = }")
except Exception as e:
    print(repr(e))

print(f'{d.get("c") = }')


# Lookup
# two modes:
# - either you found it
# - you didn't find it
#    - in-band
#    - out-of-band
# 
# OUT-OF-BAND CONSEQUENCES
# d['c'] + 1 -> KeyError: 'c' 
#
# IN-BAND CONSEQUENCES
# d.get('c') + 1 -> None + 1 -> TypeError: unsupported operand...: NoneType and int

en_es = {
    'one': 'uno',
    'two': 'dos',
    }

en_word = 'one'

# out-of-band
es_word = en_es[en_word]
print(f'To say {en_word!r} in Spanish, you say {es_word!r}')

# in-band
es_word = en_es.get(en_word)
print(f'To say {en_word!r} in Spanish, you say {es_word!r}')
