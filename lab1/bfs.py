import sys
import heapq

from maze import Maze, path_from


def dijkstra(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    start_node.visited = True
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start_node))
    while len(q) > 0:
        cost, node = heapq.heappop(q)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            newCost = node.cost + node.move_cost(child)
            if not child.visited or child.cost > newCost:
                child.parent = node
                child.cost = newCost
                heapq.heappush(q, (child.cost, child))
    return None


def greedy(maze):
    start_node = maze.find_node('S')
    start_node.cost = count_distance(start_node)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (start_node.cost, start_node))
    while len(q) > 0:
        cost, node = heapq.heappop(q)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:

            if not child.visited:
                child.parent = node
                child.cost = count_distance(child)
                heapq.heappush(q, (child.cost, child))

    return None

def astar(maze):
    start_node = maze.find_node('S')
    start_node.cost = 0
    start_node.visited = True
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (start_node.cost, start_node))
    while len(q) > 0:
        cost, node = heapq.heappop(q)  # FIFO
        node.visited = True
        if node.type == 'E':
            return path_from(node)

        children = maze.get_possible_movements(node)
        for child in children:
            newCost = node.cost + node.move_cost(child)
            if not child.visited or child.cost > newCost:
                child.parent = node
                child.cost = newCost
                heapq.heappush(q, (child.cost + count_distance(child), child))
    return None

def count_distance(node):
    end_node = maze.find_node('E')
    x = abs(node.x - end_node.x)
    y = abs(node.y - end_node.y)
    return x + y


maze = Maze.from_file(sys.argv[1])
maze.draw()
maze.path = dijkstra(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()