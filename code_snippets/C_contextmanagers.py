'''
From the @NumFOCUS telethon

title: C for contextmanager
author: @dontusethiscode
date: December 19, 2020
'''

# MOCK EXAMPLE:
# 
#    from fake_db_api import connect
#    
#    with connect() as db:
#        with db.transaction() as tx:
#            db.execute('...')
#        with db.transaction() as tx:
#            db.execute('...')
#            db.execute('...')
#            with db.transaction() as tx:
#                db.execute('...')

# CASE 1: USE CONTEXTMANAGER FROM CONTEXTLIB
from contextlib import contextmanager
from time import perf_counter
from time import sleep
            
@contextmanager
def timed(msg):
    try:
        # __enter__
        start = perf_counter()
        yield
    finally:
        # __exit__
        stop = perf_counter()
        print(f'{msg:<15} \N{greek capital letter delta}t: {stop - start:.2f}s')

print('CASE 1')
with timed('Outside elapsed'):
    sleep(1)
    with timed('Inside elapsed'):
        sleep(1)
    sleep(1)


# CASE 2: THE SAME AS A CLASS
class timed:

    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, *_):
        self.stop = perf_counter()
        print(f'{self.msg:<15} \N{greek capital letter delta}t: '
              f'{self.stop - self.start:.2f}s')

print('CASE 2')
with timed('Outside elapsed'):
    sleep(1)
    with timed('Inside elapsed'):
        sleep(1)
    sleep(1)


# EXPECTED OUTPUT:
#   
#   CASE 1
#   Inside elapsed  Δt: 1.00s
#   Outside elapsed Δt: 3.00s
#   CASE 2
#   Inside elapsed  Δt: 1.00s
#   Outside elapsed Δt: 3.00s
