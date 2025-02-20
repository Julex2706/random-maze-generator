#!/usr/bin/env python

from __future__ import print_function

import random
import sys

EMPTY = ' '
WALL = '#'
AGENT = 'o'
GOAL = 'x'

def adjacent(cell):
    i,j = cell
    for (y, x) in ((1,0), (0,1), (-1,0), (0,-1)):
        yield (i+y, j+x), (i+2*y, j+2*x)

def generate(width, height, verbose=True):
    '''
    Generates a maze as a list of strings.

    :param width: the width of the maze, not including border walls.
    :param height: the height of the maze, not including border walls.
    '''
    # add 2 for border walls.

    width += 2
    height += 2
    rows, cols = height, width

    maze = {}

    spaceCells = set()
    connected = set()
    walls = set()

    # initialize with grid.
    for i in range(rows):
        for j in range(cols):
            if (i%2 == 1) and (j%2 == 1):
                maze[(i,j)] = EMPTY
            else:
                maze[(i,j)] = WALL
    
    # Fill in border.
    for i in range(rows):
        maze[(i,0)] = WALL
        maze[(i,cols-1)] = WALL
    for j in range(cols):
        maze[(j,0)] = WALL
        maze[(j,rows-1)] = WALL
    
    for i in range(rows):
        for j in range(cols):
            if maze[(i,j)] == EMPTY:
                spaceCells.add((i,j))
            if maze[(i,j)] == WALL:
                walls.add((i,j))
    
    # Prim's algorithm to knock down walls.
    originalSize = len(spaceCells)
    connected.add((1,1))
    while len(connected) < len(spaceCells):
        doA, doB = None, None
        cns = list(connected)
        random.shuffle(cns)
        for (i,j) in cns:
            if doA is not None: break
            for A, B in adjacent((i,j)):
                if A not in walls:
                    continue
                if (B not in spaceCells) or (B in connected):
                    continue
                doA, doB = A, B
                break
        A, B = doA, doB
        maze[A] = EMPTY
        walls.remove(A)
        spaceCells.add(A)
        connected.add(A)
        connected.add(B)
        if verbose:
            cs, ss = len(connected), len(spaceCells)
            cs += (originalSize - ss)
            ss += (originalSize - ss)
            if cs % 10 == 1:
                print('%s/%s cells connected ...' % (cs, ss), file=sys.stderr)
    
    #