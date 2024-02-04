import json
import heapq
import os
import time


class Node:
    def __init__(self, x, y, cost, prev):
        self.x = x
        self.y = y
        self.cost = cost
        self.prev = prev

    def __lt__(self, other):
        return self.cost < other.cost

def wait_for_file(filename):
    """Wait for the specified file to exist before proceeding."""
    while not os.path.exists(filename):
        print(f"Waiting for {filename}...")
        time.sleep(1)  # Wait for 1 second before checking again
    print(f"Found {filename}, proceeding with A* solver.")


def load_maze(filename='/app/data/maze.txt'):
    with open(filename, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    return maze


def save_solved_maze(maze, filename='/app/data/solved_maze.txt'):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(row) + '\n')


def a_star(maze, start, end):
    start_node = Node(start[0], start[1], 0, None)
    open_list = []
    heapq.heappush(open_list, (0, start_node))
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)
        visited.add((current.x, current.y))

        if (current.x, current.y) == end:
            path = []
            while current.prev:
                path.append((current.x, current.y))
                current = current.prev
            path.append(start)
            return path[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current.x + dx, current.y + dy

            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '|' and (x, y) not in visited:
                g = current.cost + 1
                h = heuristic(x, y, end[0], end[1])
                f = g + h

                print(
                    f"Estimating path to ({x}, {y}):\n g={g}, h={h}, \n  f={g + h}")  # Printing the path estimation info,
                # g= actual cost, h= heuristic estimate,
                # f= total estimate

                heapq.heappush(open_list, (f, Node(x, y, g, current)))

    return None

def main():
    maze_file = '/app/data/maze.txt'
    solved_maze_file = '/app/data/solved_maze.txt'

    # Wait for the maze to be generated
    wait_for_file(maze_file)

    # Now we can be sure that the maze has been generated
    maze = load_maze(maze_file)
    start = (0, 0)  # Start position
    end = (len(maze) - 1, len(maze[0]) - 1)  # End position or goal

    # Run A* algorithm
    path = a_star(maze, start, end)

    if path:
        print(f"Path found: {path}")
        for x, y in path:
            if (x, y) != start and (x, y) != end:  # Don't overwrite start/end points
                maze[x][y] = 'P'  # Mark the path on the maze
        save_solved_maze(maze, solved_maze_file)
        print(f"Maze solved and saved to {solved_maze_file}")
    else:
        print("No path found.")


if __name__ == '__main__':
    main()
