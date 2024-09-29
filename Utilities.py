def path_printer(maze, path, start, end):
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
    else: return 2,4
def end_aligner (i):
    if i == 1:
        return 4,3
    elif i == 2:
        return 5,1
    elif i == 3:
        return 8,8
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
    total_cost = 0
    for position in path[1:]:  #Ignore the starting position cost
        x, y = position
        total_cost += maze[x][y]
    return total_cost

def calculate_manhattan_distance(star, end):
    return abs(end[0] - star[0]) + abs(end[1] - star[1])