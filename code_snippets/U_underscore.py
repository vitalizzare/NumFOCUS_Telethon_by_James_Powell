''' 
From the @NumFOCUS telethon

title: U for underscore 
author: @dontusethiscode
date: December 19, 2020
edited by: @vitalizzare
date: December 23, 2020
'''

# TYPICAL USECASES OF A UNDERSCORE
# 1) Unnamed indexing
for _ in range(10):
    pass

# 2) Unnamed unpacking
head, *_ = [1, 2, 3]
head, *_, tail = [1, 2, 3, 4]

# 3) With REPL as the reference to the last ouput
'''
In [1]: [1, 2, 3]
Out[1]: [1, 2, 3]

In [2]: xs = _

In [3]: xs == [1, 2, 3]
Out[3]: True
'''

# WARNING
# Output in IPython is saved in Out:
'''
In [1]: xs = [1, 2, 3]

In [2]: xs
Out[2]: [1, 2, 3]

In [3]: xs == Out[2]
Out[3]: True

In [4]: del xs

In [5]: 'xs' in globals()
Out[5]: False

In [6]: Out[2]
Out[6]: [1, 2, 3]
'''

# This means that you need to be careful
# with large objects in IPython and Jupyter Notebooks.
# Although the value of _ always changes, the output
# of the cell remains in memory in the Out dictionary

# To remove a variable from anywhere in IPython including
# output history, it is better to use %xdel

'''
In [1]: [1, 2, 3]
Out[1]: [1, 2, 3]

In [2]: xs = _

In [3]: xs
Out[3]: [1, 2, 3]

In [4]: Out
Out[4]: {1: [1, 2, 3], 3: [1, 2, 3]}

In [5]: %xdel xs

In [6]: Out
Out[6]: {}
'''
