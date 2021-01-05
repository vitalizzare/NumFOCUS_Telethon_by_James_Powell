''' 
From the @NumFOCUS telethon

title: D for dataclasses
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=2869
edited by: @vitalizzare
date: January 04, 2021
'''

# 3 common metaprogramming mechanisms for building classes
from dataclasses import dataclass     # class-descriptor
from enum import Enum, auto           # metaclass
from collections import namedtuple    # eval

@dataclass
class A:
    x: None
    y: None = 'default'
    
print(f'{A(1) = }')

class B(Enum):
    One = auto()
    Two = auto()

print(f'{[*B] = }')

C = namedtuple('C', 'x y')
print(f'{C(10, 20) = }')

# preserve inheritance hierarchy

@dataclass(order=True)
class A:
    a: None

class B(A):
    pass

print(f'{repr(A(1)) = }')
print(f'{repr(B(1)) = }')
print(f'{A(1) == A(2) = }')
print(f'{A(1) <= A(2) = }')
print(f'{A(1) == B(1) = }')
print(f'{isinstance(B(1), A) = }')
print(f'{B(1) < B(2) = }')   

