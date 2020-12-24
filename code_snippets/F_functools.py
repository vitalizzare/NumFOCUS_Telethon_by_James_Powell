''' 
From the @NumFOCUS telethon

title: F for functools
author: @dontusethiscode
date: December 19, 2020
edited by: @vitalizzare
date: December 24, 2020
'''

from functools import wraps, total_ordering
from time import perf_counter
from time import sleep


# WRAPS

def slow():
    sleep(1)

def timed(f):
    start = perf_counter()
    f()
    stop = perf_counter()
    print(f'Elapsed: {stop - start:.2f}s')

print('Process Wrapped in Function')
timed(slow)
timed(slow)
timed(slow)

def timed(f):
    def inner(*args, **kwargs):
        start = perf_counter()
        rv = f(*args, **kwargs)
        stop = perf_counter()
        print(f'Elapsed: {stop - start:.2f}s')
        return rv
    return inner

timed_slow = timed(slow)

print('Decorated Function')
timed_slow()
timed_slow()
timed_slow()

@timed
def slow():
    '''Do something slowly'''
    sleep(1)

print(f'{slow.__doc__ = }')

def timed(f):
    '''Corrected wrapper'''

    def inner(*args, **kwargs):
        start = perf_counter()
        rv = f(*args, **kwargs)
        stop = perf_counter()
        print(f'Elapsed: {stop - start:.2f}s')
        return rv

    inner.__name__ = f.__name__
    inner.__doc__ = f.__doc__

    return inner

@timed
def slow():
    '''Do something slowly'''
    sleep(1)

print(f'{slow.__doc__ = }')

def timed(f):
    '''Correct doc string with wraps'''

    @wraps(f)
    def inner(*args, **kwargs):
        start = perf_counter()
        rv = f(*args, **kwargs)
        stop = perf_counter()
        print(f'Elapsed: {stop - start:.2f}s')
        return rv

    return inner

@timed
def slow():
    '''Do something slowly'''
    sleep(1)

print(f'{slow.__doc__ = }')


# TOTAL_ORDERING

from enum import Enum, auto

@total_ordering
class Card(Enum):
    Two = auto()
    Three = auto()
    Four = auto()
    Five = auto()

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    # total_ordering provides all the other comparison operations
    
print('total_ordering usage'.upper())
print(f'{Card.Two <= Card.Two = }')
print(f'{Card.Five > Card.Two = }')
