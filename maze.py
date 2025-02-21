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

def clear_screen():
    # Funktion to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(maze, width, height):
    # Print the maze state to the console
    clear_screen() # Clear the screen before printing the updated maze
    for y in range(height):
        line = ''.join(maze[(x, y)] for x in range(width))
        print(line)
    print("\n") # Blank line after the maze

def generate(width, height, verbose=True):
    # Add 2 for border walls
    width += 2
    height += 2
    maze = {}

    # Initialize grid with walls
    for y in range(height):
        for x in range(width):
            if x % 2 == 1 and y % 2 == 1:
                maze[(x, y)] = EMPTY # Space cells
            else:
                maze[(x, y)] = WALL # Wall cells
    
    # Fill in border walls
    for x in range(width):
        maze[(x, 0)] = WALL
        maze[(x, height - 1)] = WALL
    for y in range(width):
        maze[(0, y)] = WALL
        maze[(width - 1, y)] = WALL
    
    # Initialize visited set and stack for backtracking
    visited = set()
    stack = []

    # Start at the bottom left corner (coordinates: (1, height-2))
    start = (1, height-2)
    visited.add(start)
    stack.append(start)

    # Start building the maze
    while stack:
        x, y = stack[-1]
        # Randomly shuffle directions to ensure the maze looks random
        random.shuffle(DIRS)
        found = False

        # Try all 4 directions
        for dx, dy in DIRS:
            nx, ny = x + dx * 2, y + dy * 2 # Check two steps ahead (ensures we don't overwrite walls)
        
            # Check if the next cell is within bounds and hasn't been visited
            if is_valid_move(nx, ny, width, height) and (nx, ny) not in visited:
                # Remove the wall between (x, y) and (nx, ny)
                maze[(x + dx, y + dy)] = EMPTY
                visited.add((nx, ny))
                stack.append((nx, ny))

                # Set the current path cell to '•'
                maze[(nx, ny)] = VISITED
                print_maze(maze, width, height)
                time.sleep(1) # Pause for 1 second to visualize the move
                found = True
                break # Found a valid move, break the loop and continue
        
        # If we didn't find a valid move, backtrack
        if not found:
            # Pop the stack and change the current cell back to empty
            last_x, last_y = stack.pop()
            maze[(last_x, last_y)] = EMPTY
            print_maze(maze, width, height)
            time.sleep(1) # Pause for 1 second to visualize the move
    
    # Insert character and goals
    maze[start] = AGENT
    goal = (width-2, 1)
    maze[goal] = GOAL

    # Convert the maze dict to a list of strings for display
    maze_lines = []
    for y in range(height):
        line = ''.join(maze[(x, y)] for x in range(width))
        maze_lines.append(line)
    
    return maze_lines

if __name__ == '__main__':
    width = 9
    height = 9

    maze = generate(width, height)

    # Print final maze after generation
    print('\n'.join(maze))