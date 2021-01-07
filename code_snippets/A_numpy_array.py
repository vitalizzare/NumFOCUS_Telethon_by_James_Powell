''' 
From the @NumFOCUS telethon

title: A for numpy.array
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=1855
edited by: @vitalizzare
date: January 07, 2021
'''

from numpy import array

xs = [1, 2, 3]   # fixed shape, dynamic size
ys = [4, 5, 6]
print(f'{xs + ys = }')   # structure-wise, concatenation
print(f'{xs * 3 = }')   # repetition

xs = array([1, 2, 3])   # dynamic shape, fixed size
ys = array([4, 5, 6])
print(f'{xs + ys = }')   # element-wise
print(f'{xs * 3 = }')   # element-wise
print(f'{xs.__array_interface__ = }')
print(f'{xs.__array_interface__["data"][0] = :#_x}')

print(f'\n{xs.dtype = }')
print(f'{xs = }')
xs.dtype = 'int8'
print(f'\n{xs.dtype = }')
print(f'{xs = }')

xs = array([1, 2, 3, 4])
print(f'\n{xs = }')
print(f'{xs.reshape(2, 2) = }')
