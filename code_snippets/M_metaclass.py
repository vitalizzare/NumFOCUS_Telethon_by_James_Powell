''' 
From the @NumFOCUS telethon

title: M for metaclass
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=8152
edited by: @vitalizzare
date: December 28, 2020
'''

# New objects directly inherit from `object`
class A(object):
    pass

# ... inherit from something, that inherit from `object`
class B(A):
    pass

# ... or object has a metaclass
class C:
    class __metaclass__(type):
        pass


# Suppose we have

class Base:
    def foo(self):
        print('Base.foo is applied')

# It is possible to create constraints on the Base from Derived
# to be sure we can run foo()

if not hasattr(Base, 'foo'):
    raise TypeError('Base is improperly provided')

class Derived(Base):
    def bar(self):
        print('Derived.bar is applied')
        return self.foo()

x = Derived()
print('New Derived object is created')
x.bar()

del Base, Derived, x


# The other way around: you control the Base class
# and you have some constraint that you want to enforce
# from the Base to the Derived.

print('CASE 1: __build_class__')

class Base:
    def bar(self):
        return self.foo()

import builtins
original_bc = __build_class__

def bc(func, name, *bases, bc_=original_bc, **kwargs):
    obj = bc_(func, name, *bases, **kwargs)
    if Base in bases:
        if not hasattr(obj, 'foo'):
            msg = f'CASE 1: Class `{name}` should implement the method `foo`'
            raise TypeError(msg)
    return obj

builtins.__build_class__ = bc

try: 
    class Derived(Base):
        pass
    print('CASE 1: Derived created')
except TypeError as e:
    print(repr(e))

builtins.__build_class__ = original_bc
try:
    assert 'Derived' not in globals()
except AssertionError:
    del Derived
del Base, bc, original_bc


print('CASE 2: metaclass')

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'foo' not in body:
            msg = f'CASE 2: Class `{name}` should implement the method `foo`'
            raise TypeError(msg)
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def bar(self):
        return self.foo()

    def foo():
        raise NotImplementedError()

try:
    class Derived(Base):
        pass
    print('CASE 2: Derived created')
except TypeError as e:
    print(repr(e))

try:
    assert 'Derived' not in globals()
except AssertionError:
    del Derived
del BaseMeta, Base


print('CASE 3: __init_subclass__')

class Base:

    def bar(self):
        return self.foo()

    def __init_subclass__(cls):
        if not hasattr(cls, 'foo'):
            name = cls.__name__
            msg = f'CASE 3: Class `{name}` should implement the method `foo`'
            raise TypeError(msg)

try:
    class Derived(Base):
        pass
    print('CASE 3: Derived created')
except TypeError as e:
    print(repr(e))
