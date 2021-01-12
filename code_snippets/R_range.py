''' 
From the @NumFOCUS telethon

title: R for range
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=11559
edited by: @vitalizzare
date: January 12, 2021
'''

print(f'{[*range(10)] = }')

from random import randint, randrange

print(f'{randint(0, 0) = }')        # include the last item of an interval
try:
    print(f'{randrange(0, 0) = }')  # exclude the last item of an interval
except ValueError as e:
    print(repr(e))

# example of excluding the last element of a sequence
#       01234
xs = [*'abcde']
print(f'{xs = }')
print(f'{xs[:3] = }')

# example of including the last element of a sequence
from numpy import linspace
print(f'{linspace(0, 10, 11) = }')

# another example of breaking the convention
# for the right edge of the sequence to remain open
from pandas import Series
s = Series([1, 2, 3], index=[0, 1, 2])
print(f'{s = }')
print(f'{s.iloc[0:2] = }')
print(f'{s.loc[0:2] = }')
print(f'{s.index.is_monotonic = }')

s = Series([1, 2, 3], index=[*'abc'])
print(f'{s = }')
print(f'{s.iloc[:2] = }')
print(f'{s.loc[:"c"] = }')
print(f'{s.index.is_monotonic = }')
