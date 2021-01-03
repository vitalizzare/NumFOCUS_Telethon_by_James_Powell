''' 
From the @NumFOCUS telethon

title: B for breakpoint
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=2181
edited by: @vitalizzare
date: January 03, 2021
'''

def f():
    return g()
def g():
    return h()
def h():
    return 0 / 0

# CASE 1

print('Run h() inside try-except with pdb.post_mortem:')
print('-----------------------------------------------')
from dis import dis
dis(h)

try:
    f()
except Exception:
    from pdb import post_mortem
    post_mortem()


# CASE 2

print('Run h() with `breakpoint`:')
print('--------------------------')

def h():
    breakpoint()
    return 0 / 0

from dis import dis
dis(h)

f()

# CASE 3

print('Run h() with custom `breakpoint`:')
print('---------------------------------')

import sys
from inspect import currentframe, getouterframes
from pprint import pprint

def breakpointhook():
    for f in getouterframes(currentframe())[1:-1]:
        print(f.function, f.frame.f_lineno, f.frame.f_locals)

sys.breakpointhook = breakpointhook

def f(x):
    y = x * 2
    return g(y)
def g(y):
    z = y**2
    return h(z)
def h(z):
    breakpoint()
    return z

f(10)
