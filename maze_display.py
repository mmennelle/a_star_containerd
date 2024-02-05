import json
import numpy as np
import matplotlib.pyplot as plt

def load_solved_maze(filename='/data/solved_maze.txt'):
    with open(filename, 'r') as f:
       maze = [list(line.strip()) for line in f.readlines()]
    return maze

def display_maze(maze):
    cmap = {'_': [255, 255, 255], '|': [0, 0, 0], 'S': [0, 255, 0], 'E': [255, 0, 0], 'P': [0, 0, 255]}
    rows, cols = len(maze), len(maze[0])

    grid = np.zeros((rows, cols, 3), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            grid[i, j] = cmap[maze[i][j]]

    plt.imshow(grid)
    plt.title('Maze with Path')
    plt.show()

def main():
    maze = load_solved_maze()
    display_maze(maze)

if __name__ == '__main__':
    main()
