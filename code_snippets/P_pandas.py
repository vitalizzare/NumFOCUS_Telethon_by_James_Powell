''' 
From the @NumFOCUS telethon

title: P for pandas
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=10628
edited by: @vitalizzare
date: January 06, 2021
'''

from numpy import array, nan
xs = array([1, 2, 3])
print(f'{xs * 2 = }', f'{xs.dtype = }')
xs = array([1, 2, 3, nan, nan])
print(f'{xs * 2 = }', f'{xs.dtype = }')

from pandas import array
xs = array([1, 2, 3])
print(f'{xs * 2 = }')
xs = array([1, 2, 3, nan, nan])
print(f'{xs * 2 = }')

from pandas import Series
s = Series([1, 2, 3], index=[2, 1, 0])
print(s)
print(f'{s[0] = }')
print(f'{s[0:1] = }')
print(f'{s.loc[0] = }')
print(f'{s.iloc[0] = }')

from pandas import DataFrame
from numpy.random import choice, normal
from string import ascii_lowercase
df = DataFrame({
    'ticker': choice([*ascii_lowercase], size=((size:=10), 4)).view('<U4').ravel(),
    'price': normal(size=size)
})
df = df.set_index('ticker')
print(df)
print(df.index)
print(df.columns)
print(df._data)
print(df.stack())
print(df.unstack())
print(df.melt())
