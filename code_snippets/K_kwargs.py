''' 
From the @NumFOCUS telethon

title: K for **kwargs
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=7475
edited by: @vitalizzare
date: January 03, 2021
'''

def f(*args, **kwargs):
    pass
    
f(1, 2, 3, 4, a=1, b=2, c=3)

from contextlib import contextmanager
from time import sleep, perf_counter

@contextmanager
def timed(msg):
    try:
        start = perf_counter()
        yield
    finally:
        stop = perf_counter()
        print(msg, f'{stop - start:.6f}s')

print('\nCASE 1: lru_cache\n')

from functools import lru_cache

@lru_cache
def add(x, y):
    sleep(1)
    return x + y

with timed('...'):
    print(f'{add(1, 1) = }')
with timed('...'):
    print(f'{add(1, 1) = }')
with timed('...'):
    print(f'{add(x=1, y=1) = }')
with timed('...'):
    print(f'{add(x=1, y=1) = }')

print('\nCASE 2: custom cache\n')

from inspect import signature

class memoize(dict):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        params = signature(self.f).bind(*args, **kwargs)
        key = params.args, frozenset(params.kwargs.items())
        return self[key]
    def __missing__(self, key):
        args, kwargs = key
        rv = self.f(*args, **dict(kwargs))
        self[key] = rv
        return rv

@memoize
def add(x, y):
    sleep(1)
    return x + y

with timed('...'):
    print(f'{add(2, 2) = }')
with timed('...'):
    print(f'{add(2, 2) = }')
with timed('...'):
    print(f'{add(x=2, y=2) = }')
with timed('...'):
    print(f'{add(x=2, y=2) = }')

