''' 
From the @NumFOCUS telethon

title: X for xarray
author: @dontusethiscode
date: December 19, 2020
python version: >= 3.8
video: https://youtu.be/gzbmLeaM8gs?t=14915
edited by: @vitalizzare
date: December 27, 2020
'''

from xarray import DataArray
from numpy.random import choice 

# 30 steps with 6 pieces on 8x8 board
board = choice([True, False], size=(30, 6, 8, 8))

print(board)
print(board.sum(axis=(1, 2, 3)))
print(board[:, 0, :, :])

# Let's wrap numpy.ndarray with DataArray
board = DataArray(
    choice([True, False], size=(30, 6, 8, 8)),
    dims = ['move', 'piece', 'x', 'y']
    ) 

# Previous approach still works
print(board)
print(board.sum(axis=(1, 2, 3)))
print(board[:, 0, :, :])

# But now we can additionally access to the axes by names
print(board.sum(dim=('piece', 'x', 'y')))
print(board.sel(piece=0))

# Add coordinates
board = DataArray(
    choice([True, False], size=(30, 6, 8, 8)),
    dims = ['move', 'piece', 'x', 'y'],
    coords = {
        'piece': 'Pawn Rook Knight Bishop Queen King'.split(),
        }
    ) 

print(board.sel(piece='Pawn'))
print(board.sel(piece='Pawn', x=[3, 4], y=[4, 6]))
