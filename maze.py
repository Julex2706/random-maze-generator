import random
import sys
import os
import time

EMPTY = ' '
WALL = '#'
AGENT = 'o'
GOAL = 'x'
VISITED = '•' # Symbol for showing the path during generation

# Directions for moving (up, right, down, left)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def is_valid_move(x, y, width, height):
    return 0 <= x <= width and 0 <= y <= height

