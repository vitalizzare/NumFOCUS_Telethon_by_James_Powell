''' 
From the @NumFOCUS telethon

title: E for eval and exec
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=3173
edited by: @vitalizzare
date: December 28, 2020
'''

#eval evaluates expressions
print(f"{eval('1 + 1') = }")

# exec evaluates statements
exec('''
x = 1
y = 2
print(f'{x + y = }')
''')

print(f'{x = }')
print(f'{y = }')

exec('''
x = 100 * 300
y = 2**8
''', (ns:={}))

print(f"{ns['x'] = }")
print(f"{ns['y'] = }")


# exec is not more dangerous than importing some code
from pathlib import Path
import sys

def __import__(mod):
    print('Importing', mod)
    filename = Path(mod).with_suffix('.py')
    with open(filename) as f:
        exec(f.read(), (ns:={}))
    sys.modules[mod] = ns


# the same about eval, which works like this
with open('mod.py', 'w') as f:
    f.write('print("Hello there!")\n')
    f.write('val = 42')

import mod
print(f'{mod.val = }')

Path('mod.py').unlink()
