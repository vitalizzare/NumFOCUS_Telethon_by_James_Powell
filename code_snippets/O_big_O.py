''' 
From the @NumFOCUS telethon

title: O for big-O
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=8840
edited by: @vitalizzare
date: January 03, 2021
'''

from time import perf_counter_ns, sleep
from contextlib import contextmanager

@contextmanager
def timed(msg):
    try:
        start = perf_counter_ns()
        yield
    finally:
        stop = perf_counter_ns()
        print(f'{msg:<20} \N{greek capital letter delta}t: {stop - start:10}ns')

from random import randrange
from numpy import logspace

for size in map(int, logspace(0, 5, 6)):
    xs = [randrange(-1_000, 1_000) for _ in range(size)]
    with timed(f'list {size}'):
        2000 in xs 

for size in map(int, logspace(0, 5, 6)):
    xs = {randrange(-1_000, 1_000) for _ in range(size)}
    with timed(f'set {size}'):
        2000 in xs 

