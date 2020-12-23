''' 
From the @NumFOCUS telethon

title: T for tuple
author: @dontusethiscode
date: December 19, 2020
'''

# A hacky way to change tuples
# See detailes in T_tuple_edited.py

from numpy.lib.stride_tricks import as_strided
from numpy import array

t = 1, 2, None, 4, 5
xs = array([], dtype='uint64')
offset = id(t) - xs.__array_interface__['data'][0]
ys = as_strided(xs, strides=(1,), shape=(offset+1,))
zs = as_strided(ys[offset:], strides=(8,), shape=(4,))
ws = as_strided(zs[3:], strides=(8,), shape=(len(t)+1,))
print(ws)
ws[2] = id(3)
print(t)
