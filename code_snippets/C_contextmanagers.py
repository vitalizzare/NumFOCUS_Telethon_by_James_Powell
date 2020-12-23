''' MOCK EXAMPLE:

from fake_db_api import connect

with connect() as db:
    with db.transaction() as tx:
        db.execute('...')
    with db.transaction() as tx:
        db.execute('...')
        db.execute('...')
        with db.transaction() as tx:
            db.execute('...')
'''

from contextlib import contextmanager
from time import perf_counter
            
@contextmanager
def timed(msg):
    try:
        # __enter__
        start = perf_counter()
        yield
    finally:
        # __exit__
        stop = perf_counter()
        print(f'Elapsed \N{greek capital letter delta}t: {stop - start:.2f}s')

from time import sleep

'''
Expected output:
    Elapsed Δt: 1.00s
    Elapsed Δt: 3.00s
'''
with timed('sleep(1)'):
    sleep(1)
    with timed('section: sleep(1)'):
        sleep(1)
    sleep(1)


