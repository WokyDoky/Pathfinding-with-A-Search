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
def astar(maze, start, end, allow_diagonal_movement=False):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = set()
    open_dict = {start_node.position: start_node}

    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    if allow_diagonal_movement:
        adjacent_squares += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == end_node:
            return return_path(current_node)

        children = []

        for new_position in adjacent_squares:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if (node_position[0] < 0 or node_position[0] >= len(maze) or
                node_position[1] < 0 or node_position[1] >= len(maze[0])):
                continue

            terrain_cost = maze[node_position[0]][node_position[1]]
            if terrain_cost == 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child.position in closed_list:
                continue

            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.h = np.sqrt((child.position[0] - end_node.position[0]) ** 2 +
                              (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if child.position in open_dict and child.g >= open_dict[child.position].g:
                continue

            heapq.heappush(open_list, child)
            open_dict[child.position] = child

    warn("Couldn't get a path to destination")
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