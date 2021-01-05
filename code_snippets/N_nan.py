''' 
From the @NumFOCUS telethon

title: N for nan
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=8507
edited by: @vitalizzare
date: January 05, 2021
'''

print('------------------------')
print("float('nan')")
a = float('nan')
b = float('nan')
print(f'{a == b = }')
print(f'{a is b = }')
print(f'{repr(a) = }')
print(f'{type(a) = }')

print('------------------------')
print("math.nan")
import math
a = math.nan
b = math.nan
print(f'{a == b = }')
print(f'{a is b = }')
print(f'{repr(a) = }')
print(f'{type(a) = }')

print('------------------------')
print("numpy.nan")
import numpy
a = numpy.nan
b = numpy.nan
print(f'{a == b = }')
print(f'{a is b = }')
print(f'{repr(a) = }')
print(f'{type(a) = }')

print('------------------------')
# float('nan') is not a singleton
print(f'{numpy.nan is math.nan = }')
print(f"{numpy.nan is float('nan') = }")
print(f"{math.nan is float('nan') = }")

print('------------------------')
x = float('nan')
print(f'{x = }')
print(f'{x is x = }')
print(f'{x == x = }')

class T:
    def __eq__(self, other):
        return False

t = T()
print(f'{t = }')
print(f'{t is t = }')
print(f'{t == t = }')

print('------------------------')
xs = [float('nan'), float('nan')]
ys = {float('nan'), float('nan')}
zs = (float('nan'), float('nan'))
print(f'{xs = }')
print(f'{ys = }')
print(f'{zs = }')
print(f'{xs == xs = }')
print(f'{ys == ys = }')
print(f'{zs == zs = }')

print('------------------------')
xs = numpy.array([numpy.nan])
print(f'{xs = }')
print(f'{xs == xs = }')
print(f'{numpy.array_equal(xs, xs) = }')

print('------------------------')

xs = [1, 2, 3]
if xs:
    print(f'{xs = } is not empty')

xs = numpy.array(xs)
try:
    if xs:
        print(f'{xs = } is not empty')
except Exception as e:
    print(repr(e))

if xs.any():
    print(f'{xs = } is not empty')  

xs = numpy.array([numpy.nan])
if xs.any():
    print(f'{xs = } is not empty')  
else:
    print(f'{xs = } is empty')  
    
xs = numpy.array([0, 0])
if xs.any():
    print(f'{xs = } is not empty')  
else:
    print(f'{xs = } is empty')  
    
xs = numpy.array([0])
if xs.size > 0:
    print(f'{xs = } is not empty')  
else:
    print(f'{xs = } is empty')  
