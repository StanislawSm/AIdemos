import sys


class Node:
    def __init__(self, x, y, type='.'):
        self.x = x
        self.y = y
        self.type = type
        self.visited = False
        self.parent = None
        self.cost = sys.maxsize  # Inf In one task it will be modified

    def __str__(self):
        if self.type == '.' and self.visited:
            return '_'
        elif self.type == '!' and self.visited:
            return '-'
        else:
            return self.type

    def __lt__(self, other):
        return self.move_cost(self) < other.move_cost(other)

    def move_cost(self, n2):
        if n2.type == '!':
            return 5
        else:
            return 1


class Maze:
    @classmethod
    def from_file(cls, path):
        maze = []
        with open(path) as f:
            for y, line in enumerate(f):
                x_nodes = []
                for x, char in enumerate(line.strip()):
                    x_nodes.append(Node(x, y, char))
                maze.append(x_nodes)
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze
        self.path = []



    def draw(self):
        for x_nodes in self.maze:
            for node in x_nodes:
                if node in self.path and node.type != 'S' and node.type != 'E':
                    print('*', end='')
                else:
                    print(node, end='')
            print()

    def find_node(self, type):
        for x_nodes in self.maze:
            for node in x_nodes:
                if node.type == type:
                    return node

    def get_possible_movements(self, node):
        possible_movements = []
        if node.y - 1 >= 0 and self.maze[node.y - 1][node.x].type != '#':  # north
            possible_movements.append(self.maze[node.y - 1][node.x])
        if node.x + 1 < len(self.maze[node.y]) and self.maze[node.y][node.x + 1].type != '#':  # east
            possible_movements.append(self.maze[node.y][node.x + 1])
        if node.y + 1 < len(self.maze) and self.maze[node.y + 1][node.x].type != '#':  # south
            possible_movements.append(self.maze[node.y + 1][node.x])
        if node.x - 1 >= 0 and self.maze[node.y][node.x - 1].type != '#':  # west
            possible_movements.append(self.maze[node.y][node.x - 1])

        return possible_movements




def path_from(node):
    path = [node]
    while node.parent is not None:
        node = node.parent
        path.append(node)
    return path