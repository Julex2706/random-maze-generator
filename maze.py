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
    for (y,x) in ((1,0), (0,1), (-1,0), (0,-1)):
        yield (i+y, j+x), (i+2*y, j+2*x)

