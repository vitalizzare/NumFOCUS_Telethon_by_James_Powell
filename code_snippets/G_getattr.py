''' 
From the @NumFOCUS telethon

title: G for getattr
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=4861
edited by: @vitalizzare
date: January 07, 2021
'''

class A:
    
    z = 300
    
class B(A):

    y = 20

    def __init__(self):
        self.x = 1

def _getattr(obj, attr):
    if attr in obj.__dict__:
        return obj.__dict__[attr]
    if attr in type(obj).__dict__:
        return type(obj).__dict__[attr]

obj = B()
print(f"{ getattr(obj, 'x') = }")
print(f"{_getattr(obj, 'x') = }")
print(f"{ getattr(obj, 'y') = }")
print(f"{_getattr(obj, 'y') = }")
print(f"{ getattr(obj, 'z') = }")
print(f"{_getattr(obj, 'z') = }")

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(f'{D.__mro__ = }')

def _getattr(obj, attr):
    if attr in obj.__dict__:
        return obj.__dict__[attr]
    for cls in type(obj).__mro__:
        if attr in cls.__dict__:
            return cls.__dict__[attr]

print(f"{ getattr(obj, 'z') = }")
print(f"{_getattr(obj, 'z') = }")

class D:

    def __get__(*_):
        return 4_000

class A:
    
    z = 300
    W = D()
    
class B(A):

    y = 20

    def __init__(self):
        self.x = 1

def _getattr(obj, attr):
    if attr in obj.__dict__:
        return obj.__dict__[attr]
    for cls in type(obj).__mro__:
        if attr in cls.__dict__:
            rv = cls.__dict__[attr]
            if hasattr(type(rv), '__get__'):
                return rv.__get__(obj, cls)
            return rv

obj = B()

print(f"{ getattr(obj, 'W') = }")
print(f"{_getattr(obj, 'W') = }")
