''' 
From the @NumFOCUS telethon

title: S for staticmethod
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=11930
edited by: @vitalizzare
date: January 12, 2021
'''

def foo(self):
    pass

class T:

    foo = foo
    from json import loads
    from itertools import count

x = T()
x.foo()                        # success
try:
    x.loads('[]')              # fail
except TypeError as e:
    print(repr(e))
print(f'{next(x.count()) = }') # success

def f():
    pass

print(f'{f.__get__ = }')


# redefine staticmethod
class static:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner):
        return self.f

class T:
    @static
    def foo():
        return 'foo'

x = T()
print(f'{x.foo() = }')

