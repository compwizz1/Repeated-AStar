# Repeated-AStar

Repeated A* is a pathfinding algorithm to navigate an agent to the goal in an area by using A* search on a map of the area with observed obstacles, moving the agent along the calculated path, and then repeating the procedure with an updated observed map when an obstacle is encountered blocking the path. At each loop iteration of an A* search, the following evaluation function f(s) is used to determine which node to explore:

	f(s) = g(s) + h(s). A next node s1 is expanded if f(s1) is the smallest of all available next states.   
	g(s): The amount of steps taken to already reach the current state s
	h(s): A heuristic used to underestimate the minimum number of steps needed to reach the goal (implemented as Manhattan distance)
	
Repeated A* terminates when either the goal is reached or an A* search cannot find a path to the goal.

To generate maps or regenerate existing maps, run the following command in terminal:

	python MapMaker.py

This creates a maps folder if it doesn't exist and then generates plaintext files named map1 to map49. A # represents an obstacle while a _ represents an empty space. S and G are the start and goal states respectively.

To run a repeated A* and get an output map with the agent's path, run the following command:

	python __A-version.py__ __Mapname__

__A-version.py__ is any .py file prefixed with A-. __Mapname__ is the name of a valid map file in the maps folder. The program either responds that a path doesn't exist or outputs a new map file marking the path the agent took with X. Additionally, the program appends (or creates and then appends) runtime and pathlength information to the results file in the root directory when a path is successfully found.


The following details how each version implements repeated A* differently:

	A-blarge.py: Runs A* search from goal state to start state. In tiebreaking the smallest f(s), the largest g(s) is used. 
	
	A-flarge.py: Runs A* serach from start state to goal state. In tiebreaking the smallest f(s), the largest g(s) is used. 

	A-fsmall.py: Runs A* serach from start state to goal state. In tiebreaking the smallest f(s), the smallest g(s) is used. 
	
	A-adapt.py: Equivalent to flarge. However, every new A* search penalizes nodes previously explored by adding to their f(s) values to promote exploring different nodes. 
