import numpy as np
import json

def generate_noise(width, height):
    return np.random.random((width, height))

def marching_squares(noise, threshold=0.2):
    maze = [['_' for _ in range(noise.shape[1])] for _ in range(noise.shape[0])]

    for x in range(1, noise.shape[0]):
        for y in range(1, noise.shape[1]):
            square = [
                noise[x - 1, y - 1] > threshold,
                noise[x, y - 1] > threshold,
                noise[x - 1, y] > threshold,
                noise[x, y] > threshold
            ]

            if sum(square) == 2:
                if square[0] == square[3]:
                    maze[x][y - 1] = '|'
                if square[1] == square[2]:
                    maze[x - 1][y] = '|'
            elif sum(square) == 1 or sum(square) == 3:
                maze[x - 1][y - 1] = '|'

    return maze

def save_maze(maze, filename='app/data/maze.txt'):
    with open(filename, 'w') as f:
        f.write(''.join(row)+"\n")

def main():
    width, height = 5, 5
    noise = generate_noise(width, height)
    maze = marching_squares(noise)
    save_maze(maze)

if __name__ == '__main__':
    main()
