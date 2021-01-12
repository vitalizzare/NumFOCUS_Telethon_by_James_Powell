''' 
From the @NumFOCUS telethon

title: I for iterator
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=5587
edited by: @vitalizzare
date: January 12, 2021
'''

xs = [1, 2, 3]
try:
    print(f'{next(xs) = }')
except TypeError as e:
    print(f'An error orrured while getting next(xs): {e!r}')

# iterator 
# - externalisation of the state of looping
# - reference to an iterable
# - some state (i.e., where you left off)

xi1 = iter(xs)
xi2 = iter(xs)
print(f'{next(xi1) = }')
print(f'{next(xi2) = }')

def f(w):
    x = w * 2
    y = w ** 2
    z = w + 2
    return x, y, z

def g(w):
    yield w * 2
    yield w ** 2
    yield w + 2

gi = g(100)
print(f'{next(gi) = }')
print(f'{gi.gi_frame.f_lasti = }')
print(f'{next(gi) = }')
print(f'{gi.gi_frame.f_lasti = }')
print(f'{next(gi) = }')
print(f'{gi.gi_frame.f_lasti = }')

from dis import dis
dis(g)

# generator is an iterable
# generator instance is an iterator
# - the underlying computation (i.e., reference to the iterable)
# - some state (i.e., where you left off, i.e., the last instruction that you computed)

xs = [1, 2, 3, 4]
xi = iter(xs)
print(f'{next(xi) = }')
print(f'{next(xi) = }')
print(f'{next(xi) = }')
print(f'{next(xi) = }')
xs.append(5)
print(f'{next(xi) = }')
xs.extend([6,7,8])
print(f'{next(xi) = }')
xs.clear()
try:
    print(f'{next(xi) = }')
except StopIteration:
    print('The next item cannot be retrieved because the iterator is exhausted.')
