''' underscore '''

# typical usecases
# 1) unnamed indexing
for _ in range(10):
    pass

# 2) unnamed unpacking
head, *_ = [1, 2, 3]
head, *_, tail = [1, 2, 3, 4]

# 3) with REPL as the reference to the last ouput
'''
>>> xs = [1, 2, 3]
>>> xs
[1, 2, 3]
>>> xs == _
True
'''

# WARNING
# with IPython
'''
In [1]: xs = [1, 2, 3]

In [2]: xs
Out[2]: [1, 2, 3]

In [3]: xs == _
Out[3]: True

In [4]: xs == Out[2]
Out[4]: True

In [5]: del xs

In [6]: 'xs' in globals()
Out[6]: False

In [7]: Out[2]
Out[7]: [1, 2, 3]
'''
# Which means one should be careful with big objects in IPython 
# (and Jupyter Notebooks). While reference of _ allways changes,
# the output of the cell stays in memory with the Out dictionary

# To delete a variable from anywhere in IPython, including 
# the output history, use %xdel
