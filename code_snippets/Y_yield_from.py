''' 
From the @NumFOCUS telethon

title: Y for yield from
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=15295
edited by: @vitalizzare
date: December 26, 2020
'''

# NOTE: for python >= 3.8 the next code will cause 
# SyntaxError: 'yield' inside generator expression
#
#     g = [[1, 2, 3], [4, 5, 6]]
#     print(list(None for g in g if (yield from g) and False))
#
# HOU IT WORKED:
# 1) '(yield from g)' added a new exit point where the elements
#        of the inner lists were returned;
# 2) 'None' at the beginning is a placeholder;
# 3) 'and False' at the end is a garantee, that nothing exept 
#        the elements from the inner lists will be passed out.
# 
# We can rewrite it this way:
# 
#     def gen(main_list):
#         for sub_list in main_list:
#             if (yield from sub_list) and False:
#                 yield None
# 
# James Powell uses here a notation like [g for g in g for g in g]
# To make things obvious, it's [i for inner in main for i in inner]

xs = [[1, 2, 3], [4, 5, 6]]

# Typical use of 'yield from'
def ys(seq):
    for inner in seq:
        yield from inner

print(f'{xs = }')
print(f'{[*ys(xs)] = }')
print(f'{[i for g in xs for i in g] = }')
print(f'{[*ys(xs)] == [i for g in xs for i in g] = }')

# Alternative
from itertools import chain
print(f'{[*chain(*xs)] = }')

def g():
    yield 1
    yield 2
    yield 3
    yield from [4, 5, 6]

print(f'{[*g()] = }')

# 'yield from' means don't yield the structure as a structure itself.
# Go into that structure and yield each individual elements.

def g(n):
    if n:
        yield 1
        yield 2
        yield 3
        yield from g(n-1)

print(f'{[*g(4)] = }')
