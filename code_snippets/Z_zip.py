''' 
From the @NumFOCUS telethon

title: Z for zip
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=15648
edited by: @vitalizzare
date: January 10, 2021
'''

xs = [1, 2, 3, 4, 5, 6, 7]
print(f'{xs = }')
for x, y, z in zip(xs[0:], xs[1:], xs[2:]):
    print(f'{x, y, z = }')

from itertools import islice, tee
nwise = lambda g, n=2: zip(*(islice(g, idx, None) for idx, g in enumerate(tee(g, n))))

for x, y, z in nwise('abcde', 3):
    print(f'{x, y, z = }')

from itertools import repeat, chain
first = lambda g, n=1: zip(chain(repeat(True, n), repeat(False)), g)

for is_first, x in first('abcde', 3):
    print(f'{is_first, x = }')

from itertools import zip_longest
nwise_longest = lambda g, n=2, fv=None: zip_longest(
                    *(islice(g, idx, None) for idx, g in enumerate(tee(g, n))),
                    fillvalue=fv)
last = lambda g, n=1, s=object(): ((y[-1] is s, x) for x, *y in nwise_longest(g, n+1, s))

for is_last, x in last('abcde', 2):
    print(f'{is_last, x = }')

for is_first, (is_last, curr) in first(last('abcd')):
    if is_first:
        print('first element is', curr)
    elif is_last:
        print('last element is', curr)
    else:
        print('...', curr)
