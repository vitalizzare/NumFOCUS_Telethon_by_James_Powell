''' 
From the @NumFOCUS telethon

title: L for len
author: @dontusethiscode
date: December 19, 2020
edited by: @vitalizzare
date: December 24, 2020
'''

from sys import version_info
assert version_info >= (3,8)

from collections.abc import Sized 

class Deck:
    
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

print('General case'.upper())
d = Deck(['4H', '3C'])
print(f'{isinstance(d, Sized) = }')
print(f'{len(d) = }')


class Hand:
    ''' Try to return a float len '''
    def __len__(self):
        return .5

print('\nCase: Float length'.upper())
print(f'{isinstance(Hand(), Sized) = }')
try:
    print(f'{len(Hand()) = }')
except TypeError as e:
    print(repr(e))


class Purse:
    ''' Try to return a negative len '''
    def __len__(self):
        return -20

print('\nCase: Negative length'.upper())
print(f'{isinstance(Purse(), Sized) = }')
try:
    print(f'{len(Purse()) = }')
except ValueError as e:
    print(repr(e))


# len() - some discrete, not negative measure of the object
# What about objects with multiple distinct notions of their length?
# It should be one unique prividge notion of what the size of the thing is.


print('\nCase: Substitute builtins length'.upper())
import builtins
builtins.len = lambda x, *, _len=len: _len(x) + 1
print(f'{len([1,2,3]) = }')
