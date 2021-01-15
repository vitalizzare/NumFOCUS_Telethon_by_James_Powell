''' 
From the @NumFOCUS telethon

title: W for walrus
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=14577
edited by: @vitalizzare
date: January 15, 2021
'''

# expression/statement dichonomy

# STATEMENTS:
def func(): pass
class T: pass
for _ in (): pass
while False: pass
if ...:
    pass
else:
    pass
x = 'something'

# EXPRESSIONS
1 + 1
'abc'.upper()
func()
x[4:]
func.__module__
'even' if len(x) % 2 == 0 else 'odd'

# expression that can bind the variable 

from re import compile as re_compile

patt1 = re_compile('abc')
patt2 = re_compile('def')

text = '''
abc
def
xyz
'''

for line in text.strip().splitlines():
    mo = patt1.fullmatch(line)
    if mo:
        print(mo)
    else:
        mo = patt2.fullmatch(line)
        if mo:
            print(mo)

# with the walrus operator
for line in text.strip().splitlines():
    if (mo := patt1.fullmatch(line)): 
        print(mo)
    elif (mo := patt2.fullmatch(line)):
        print(mo)

from pandas import DataFrame
from numpy.random import normal

df = DataFrame({
    'x': normal(size=(SIZE := 10)),
    'y': normal(size=SIZE),
    'z': normal(size=SIZE),
})
