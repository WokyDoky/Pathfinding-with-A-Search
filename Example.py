from warnings import warn
import heapq
import numpy as np
import Utilities


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

"""
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """


def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    movement_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            return return_path(current_node)

        children = []

        for move in movement_directions:
            node_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) - 1) or \
                    node_position[1] < 0:
                continue

            terrain_cost = maze[node_position[0]][node_position[1]]

            if terrain_cost == 0:
                continue

            new_node = Node(current_node, node_position)
            new_node.g = current_node.g + terrain_cost
            new_node.h = abs(new_node.position[0] - end_node.position[0]) + abs(
                new_node.position[1] - end_node.position[1])  # Manhattan distance
            new_node.f = new_node.g + new_node.h

            if len([closed_child for closed_child in closed_list if closed_child == new_node]) > 0:
                continue

            if len([open_node for open_node in open_list if
                    new_node.position == open_node.position and new_node.g > open_node.g]) > 0:
                continue

            heapq.heappush(open_list, new_node)

    warn("Couldn't find a path to the destination")
    return None


def main():

    mazeOption = 3
    maze = Utilities.maze_chooser(mazeOption)

    start = Utilities.start_aligner(mazeOption)
    end = Utilities.end_aligner(mazeOption)
    path = astar(maze, start, end)
    print(np.matrix(maze))
    print("Path cost: ", Utilities.calculate_path_cost(maze, path))
    print("Manhattan distance: ", Utilities.calculate_manhattan_distance(start, end))
    print(path)
    Utilities.path_printer(maze, path, start, end)


if __name__ == '__main__':
    main()

#Code by Nicholas Swift, modified by Jesus Daniel Benavente.