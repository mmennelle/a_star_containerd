import json
import heapq


class Node:
    def __init__(self, x, y, cost, prev):
        self.x = x
        self.y = y
        self.cost = cost
        self.prev = prev

    def __lt__(self, other):
        return self.cost < other.cost
def load_maze(filename='/app/data/maze.txt'):
    with open(filename, 'r') as f:
        maze = [list(line.strip()) for line in f.readlines()]
    return maze

def save_solved_maze(maze, filename='/app/data/solved_maze.txt'):
    with open(filename, 'w') as f:
        f.write(''.join(row) + '\n')

# Heuristic function (manhatten pattern)(small maps)
def heuristic(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)
# Heuristic function (Euclidean distance)
# def heuristic(x1, y1, x2, y2):
#   return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# Heuristic function (Chebyshev distance)
# def heuristic(x1, y1, x2, y2):
#   return max(abs(x1 - x2), abs(y1 - y2))
# Heuristic function (Diagonal distance)(Large maps)
#def heuristic(x1, y1, x2, y2):
 #   dx = abs(x1 - x2)
  #  dy = abs(y1 - y2)
   # diagonal = min(dx, dy)
    #straight = dx + dy
    #return math.sqrt(2.0) * diagonal + (straight - 2 * diagonal)


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
    maze = load_maze()
    start = (0, 0)  # Start position
    end = (len(maze) - 1, len(maze[0]) - 1)  # End position or goal
    path = a_star(maze, start, end)

    if path:
        print(f"Path found: {path}")
        # The start and end points should not be overwritten
        maze[start[0]][start[1]] = 'S'
        maze[end[0]][end[1]] = 'E'
        for x, y in path:
            if (x, y) != start and (x, y) != end:  # Don't overwrite start/end points
                maze[x][y] = 'P'  # Mark the path on the maze
        save_solved_maze(maze)  # Save the solved maze
    else:
        print("No path found.")

if __name__ == '__main__':
    main()
