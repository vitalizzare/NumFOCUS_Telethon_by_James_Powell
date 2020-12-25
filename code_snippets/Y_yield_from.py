''' 
From the @NumFOCUS telethon

title: Y for yield from
author: @dontusethiscode
date: December 19, 2020
edited by: @vitalizzare
date: December 24, 2020
'''
xs = [[1, 2, 3], [4, 5, 6]]
ys = (None for g in xs if (yield from g) and False)
print(*ys)

# NOTE: for python >= 3.8 this will cause 
# a SyntaxError: 'yield' inside generator expression
# print([None for g in g if (yield from g) and False])

# Generator ys is equal to [g for g in g for g in g]
g = [[1, 2, 3], [4, 5, 6]]
ys = (None for g in g if (yield from g) and False)
print(f'{[*ys] == [g for g in g for g in g]}')
# [item for sublist in xs for item in sublist]
g = [[1,2,3],[4,5,6]]
from itertools import chain
[*chain(*g)]
