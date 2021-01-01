''' 
From the @NumFOCUS telethon

title: Q for queue
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=11137
edited by: @vitalizzare
date: January 01, 2021
'''

# list as a stack
xs = [1, 2, 3]
print(f'{xs = }')
while xs:
    print(f'{xs.pop() = }')

# collections.deque as a stack or a queue
from collections import deque
xs = deque([1, 2, 3])
print(f'{xs = }')
while xs:
    print(f'{xs.popleft() = }')

tree = {
    'a': {'b': {'c': None, 'd': None},
          'e': {'f': None}
    } 
}

#     A
#    / \
#   B   E 
#  / \   \ 
# C   D   F

# DFS = Depth First Search = A-B-C-D-E-F

# preorder traversal
def preorder(tree, node):
    yield node
    for child in tree[node] or {}:
        yield from preorder(tree[node], child)

print(f'{[*preorder(tree, "a")] = }')

# postorder traversal
def postorder(tree, node):
    for child in tree[node] or {}:
        yield from postorder(tree[node], child)
    yield node

print(f'{[*postorder(tree, "a")] = }')

# BFS = Breadth First Search = A-B-E-C-D-F

def bfs(tree):
    state = deque(tree.items()) if tree else []
    while state:
        node, tree = state.popleft()
        yield node
        if tree:
            state.extend(tree.items())


print(f'{[*bfs(tree)] = }'

