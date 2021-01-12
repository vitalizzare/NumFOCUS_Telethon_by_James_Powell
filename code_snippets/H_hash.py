''' 
From the @NumFOCUS telethon

title: H for hash
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=5203
edited by: @vitalizzare
date: January 12, 2021
'''

# In CPython the value of hash can not be -1
class A:
    def __hash__(self):
        return -1

print(f'{hash(A()) = }')

# Caveat: you can compute the hash on a mutable object,
# but you must compute it on the identity of the immutable object
# and you will only be able to put this object in a container
# that provides intermediated access.

from networkx import DiGraph

class Node:
    def __init__(self, x=0):
        self.x = x
    def __hash__(self):
        return hash(id(self))
    def __repr__(self):
        return f'Node({self.x})'
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise NotImplementedError()
        return self.x == other.x

print(f'{Node(1) == Node(1) = }')
print(f'{Node(1) is Node(1) = }')

g = DiGraph()
x, y, z = Node(1), Node(2), Node(3)
g.add_edge(x, y)
g.add_edge(x, z)
print(f'{x = }')
print(f'{g[x] = }')
try:
    print(f'{g[Node(1)] = }')
except KeyError as e:
    print('An error occurred while trying to access g[Node(1)]:', repr(e))

# ???
# class Network:
#     def __init__(self, g):
#         self.g = DiGraph()
#         self.by_x = {}
#     def lookup(self, g):
#         self
# 
# net = Network()
# net.add_edge(Node(1), Node(2))
# net.add_edge(net.lookup(1), Node(2))
