"""

This code finds the shortest path between two points in a maze
using the A* search algorithm.
The maze is provided as a 2D array in the "Utilities.py" class.

The maze contains numbers that indicate the cost of traveling into
a particular space.
A number 0 indicates that it is not possible to enter that space.

As of right now, user can choose between two options, either
manhattan distance or Euclidean distance. User can also choose
between allowing diagonal or not. For this assignment, it will not
choose diagonal.

"""

import random
import heapq
import numpy as np
import timeit
import matplotlib.pyplot as plt

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

def heuristic_function(i, new_node, end_node):
    if i == 0: return 0;
    #Manhattan Distance
    if i == 1: return abs(new_node.position[0] - end_node.position[0]) + abs(new_node.position[1] - end_node.position[1])  # Manhattan distance.
    #Euclidean Distance
    if i == 2: return np.sqrt((new_node.position[0] - end_node.position[0]) ** 2 + (new_node.position[1] - end_node.position[1]) ** 2) # Euclidean distance.
    #Manhattan Distance with added errors.
    if i == 3: return abs(new_node.position[0] - end_node.position[0]) + abs(new_node.position[1] - end_node.position[1]) + random.randint(-3, 3)  # Manhattan distance + Random number.

"""
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return path: 
    """

def astar(maze, start, end, heuristic, allow_diagonal_movement = False):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    movement_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    if allow_diagonal_movement:
        movement_directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

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
            new_node.h = heuristic_function(heuristic, new_node, end_node)
            new_node.f = new_node.g + new_node.h

            if len([closed_child for closed_child in closed_list if closed_child == new_node]) > 0:
                continue

            if len([open_node for open_node in open_list if
                    new_node.position == open_node.position and new_node.g > open_node.g]) > 0:
                continue

            heapq.heappush(open_list, new_node)

    #warn("Couldn't find a path to the destination")
    return None


def print_info(start, end, maze, path, print_extra = False):

    print("Path cost: ", calculate_path_cost(maze, path))
    print("Manhattan distance: ", calculate_manhattan_distance(start, end))
    print(path)
    if print_extra:
        print(np.matrix(maze))
        path_printer(maze, path, start, end)

def path_printer(maze, path, start, end):
    if path is None: return "No Solution"
    print(" ", end=" ")
    for row in range(len(maze[0])): print(row, end = " ")
    print("")
    for i in range(len(maze)):
        print(i, end = " ")
        for j in range(len(maze[i])):
            if (i, j) == start:
                print("@", end = " ")
                continue
            if (i, j) == end:
                print("%", end = " ")
                continue
            elif (i, j) in path:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()  # Print a newline after each row

def start_aligner (i):
    if i == 1:
        return 1,2
    elif i == 2:
        return 3,6
    elif i == 3:
        return 1,2
    elif i == 4:
        return 1,1
    elif i == 5:
        return 2,1
    else: return 2,4
def end_aligner (i):
    if i == 1:
        return 4,3
    elif i == 2:
        return 5,1
    elif i == 3:
        return 8,8
    elif i == 4:
        return 1,7
    elif i == 5:
        return 3,7
    else: return 7,6
def maze_chooser (i):
    if i == 1:
        maze = [[2,4,2,1,4,5,2],
                [0,1,2,3,5,3,1],
                [2,0,4,4,1,2,4],
                [2,5,5,3,2,0,1],
                [4,3,3,2,1,0,1]]
        return maze
    elif i == 2:
        maze = [[1,3,2,5,1,4,3],
                [2,1,3,1,3,2,5],
                [3,0,5,0,1,2,2],
                [5,3,2,1,5,0,3],
                [2,4,1,0,0,2,0],
                [4,0,2,1,5,3,4],
                [1,5,1,0,2,4,1]]
        return maze
    elif i == 3:
        maze = [[2,0,2,0,2,0,0,2,2,0],
                [1,2,3,5,2,1,2,5,1,2],
                [2,0,2,2,1,2,1,2,4,2],
                [2,0,1,0,1,1,1,0,0,1],
                [1,1,0,0,5,0,3,2,2,2],
                [2,2,2,2,1,0,1,2,1,0],
                [1,0,2,1,3,1,4,3,0,1],
                [2,0,5,1,5,2,1,2,4,1],
                [1,2,2,2,0,2,0,1,1,0],
                [5,1,2,1,1,1,2,0,1,2]]
        return maze
    elif i == 4:
        maze = [[0, 0, 2, 0, 2, 0, 0, 2, 2, 0],
                [0, 1, 1, 1, 1, 1, 2, 5, 1, 2],
                [0, 0, 1, 2, 1, 2, 1, 2, 4, 2],
                [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
                [1, 0, 0, 0, 1, 0, 1, 2, 2, 2],
                [2, 0, 2, 2, 1, 0, 1, 2, 1, 0],
                [1, 0, 2, 1, 1, 1, 4, 3, 0, 1],
                [2, 1, 1, 1, 1, 2, 1, 2, 4, 1],
                [1, 2, 2, 2, 0, 2, 0, 1, 1, 0],
                [5, 1, 2, 1, 1, 1, 2, 0, 1, 2]]
        return maze
    elif i == 5:
        maze = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                [5, 1, 2, 3, 4, 5, 1, 2, 3, 4],
                [4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
                [3, 4, 5, 1, 2, 3, 4, 5, 1, 2],
                [2, 3, 4, 5, 1, 2, 3, 4, 5, 1],
                [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                [5, 1, 2, 3, 4, 5, 1, 2, 3, 4],
                [4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
                [3, 4, 5, 1, 2, 3, 4, 5, 1, 2],
                [2, 3, 4, 5, 1, 2, 3, 4, 5, 1]]
        return maze
    else:
        maze = [[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        return maze


def calculate_path_cost(maze, path):
    if path is None: return "No solution found"
    total_cost = 0
    for position in path[1:]:  #Ignore the starting position cost
        x, y = position
        total_cost += maze[x][y]
    return total_cost

def calculate_manhattan_distance(star, end):
    return abs(end[0] - star[0]) + abs(end[1] - star[1])


def timeing_different_heuristic_formulas(mazeOption):
    print(f"Maze: {mazeOption}")
    maze = maze_chooser(mazeOption)

    start = start_aligner(mazeOption)
    end = end_aligner(mazeOption)

    times = []

    for integer_value in range(4):  # 0 to 3
        start_time = timeit.default_timer()
        astar(maze, start, end, integer_value)  # Call your function here
        elapsed = timeit.default_timer() - start_time
        times.append(elapsed)
        print(
            f"Execution time for h({integer_value}) (Start: {start}, End: {end}): {elapsed:.10f} seconds")

    return times

def make_graph():
    heuristic_times = {i: [] for i in range(4)}  # Store times for each heuristic

    # Run the function for all maps
    for maze_option in range(1, 6):  # Assuming maps are numbered from 1 to 5
        times = timeing_different_heuristic_formulas(maze_option)
        for i, time in enumerate(times):
            heuristic_times[i].append(time)

    # Calculate average times for each heuristic function
    average_times = [sum(heuristic_times[i]) / len(heuristic_times[i]) for i in range(4)]

    # Plotting the graph
    plt.bar(range(4), average_times, color=['blue', 'green', 'red', 'orange'])
    plt.xlabel('Heuristic Function')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Average Execution Time for Heuristic Functions Across All Maps')
    plt.xticks(range(4), [f'h({i})' for i in range(4)])
    plt.show()


"""
=====================================================================================
===================================== MAIN ==========================================
=====================================================================================
"""

def main():
    #Do not use unless you want to generate graph
    #   Utilities.make_graph()
    """
    Code might look weird since it was originally two files with a utility class.
    Had to merge them for this assignment.
    If the original code wants to be seen follow this link:
    https://github.com/WokyDoky/Pathfinding-with-A-Search/blob/addingMoreHeuristicValues/Utilities.py
    """
    print("Enter 2 values, first value will choose a map, second value will choose a heuristic.")
    print("Values for the map range from 1 - 5 and for the heuristic value from 1 - 4.")

    # Read input and split, then cast to integers
    value1, value2 = map(int, input("Separate values by a space > ").split())

    maze_option = value1
    maze = maze_chooser(maze_option)

    start = start_aligner(maze_option)
    end = end_aligner(maze_option)

    path = astar(maze, start, end, value2)

    print_info(start, end, maze, path)


if __name__ == '__main__':
    main()

#Code by Nicholas Swift, modified by Jesus Daniel Benavente.