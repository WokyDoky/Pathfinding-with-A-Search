# Pathfinding-with-A-Search

Pathfinding	is a common	problem	that artificial	agents	must solve,	including
mapping services, artificial vehicles, AIs in real-time strategy games, and robots that	
must navigate in the physical world. For this assignment we	will focus on simplified	
pathfinding	problem.

This code finds the shortest path between two points in a maze
using the A* search algorithm.

~~The maze is provided as a 2D array in the "Utilities.py" class.~~
This used to be the case but now everything is in one class. 
If you wish to see the original, traverse the latest [branch](https://github.com/WokyDoky/Pathfinding-with-A-Search/tree/willMergeToMain).



The maze contains numbers that indicate the cost of traveling into
a particular space.
A number 0 indicates that it is not possible to enter that space.

User can choose between 4 distinct heuristic functions. User can also choose
between allowing diagonal movement or not. For this assignment, it will not
choose diagonal as default.

> Assumptions:
>* The code will not loop to chose other maps.