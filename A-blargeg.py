from __future__ import print_function
import sys
import os
import random
import numpy
import heapq

xstart = None
ystart = None
xgoal = None
ygoal = None
agentx = None
agenty = None

knownmap = [['_' for i in range(0, 101)] for j in range (0, 101)]

opened = []
closed = []
global acounter
acounter = 0
class node:
	y = None
	x = None
	gval = None
	hval = None
	parent = None
	child = None
	def __init__(self, y, x, gval, parent):
		self.y = y
		self.x = x
		self.gval = gval
		self.hval = abs(self.y - agenty) + abs(self.x - agentx)
		self.parent = parent
	def fval(self):
		return self.gval + self.hval
	def __cmp__(self, other):
		if other == None:
			return -1
		if self.fval() == other.fval():
			if(self.gval == other.gval):
				#prioritize going down over going right
				if(self.y == other.y):
					return cmp(self.x, other.x)
				else:
					return cmp(self.y, other.y)
			else:
				#large g prioritized
				return -cmp(self.gval, other.gval)
		return cmp(self.fval(), other.fval())

def astar():
	parent = opened[0]
	closed[parent.y][parent.x] = True
	while len(opened) != 0 and not (parent.x == agentx and parent.y == agenty):
		parent = heapq.heappop(opened)
		if parent.x > 0 and closed[parent.y][parent.x - 1] == False and knownmap[parent.y][parent.x - 1] != 'X':
			closed[parent.y][parent.x - 1] = True
			heapq.heappush(opened, node(parent.y, parent.x - 1, parent.gval + 1, parent) )
		if parent.x < 100 and closed[parent.y][parent.x + 1] == False and knownmap[parent.y][parent.x + 1] != 'X':
			closed[parent.y][parent.x + 1] = True
			heapq.heappush(opened, node(parent.y, parent.x + 1, parent.gval + 1, parent) )
		if parent.y > 0 and closed[parent.y - 1][parent.x] == False and knownmap[parent.y - 1][parent.x] != 'X':
			closed[parent.y - 1][parent.x] = True
			heapq.heappush(opened, node(parent.y - 1, parent.x, parent.gval + 1, parent) )
		if parent.y < 100 and closed[parent.y + 1][parent.x] == False and knownmap[parent.y + 1][parent.x] != 'X':
			closed[parent.y + 1][parent.x] = True
			heapq.heappush(opened, node(parent.y + 1, parent.x, parent.gval + 1, parent) )
		#print(str(parent.x) + ' ' + str(parent.y) + ' ' + str(len(opened)))
		global acounter 
		acounter = acounter + 1
	if not (parent.x == agentx and parent.y == agenty):
		return None
	ptr = parent
	return ptr

if __name__ == "__main__":
	#retrieve map from file specified in command line
	with open('./maps/' + sys.argv[1], 'r') as file:
		data = file.readlines()
	map = []
	vistednodes = []
	linecount = 0
	for line in data:
		linelist = line.split()
		if 'S' in linelist:
			xstart = linelist.index('S')
			ystart = linecount
			agentx = xstart
			agenty = ystart
		if 'G' in linelist:
			xgoal = linelist.index('G')
			ygoal = linecount		
		map.append(linelist)
		linecount = linecount + 1
	#repeated A* code
	knownmap[agenty][agentx] = map[agenty][agentx]
	if agentx > 0:
		knownmap[agenty][agentx - 1] = map[agenty][agentx - 1]
	if agentx < 100:
		knownmap[agenty][agentx + 1] = map[agenty][agentx + 1]
	if agenty > 0:
		knownmap[agenty - 1][agentx] = map[agenty - 1][agentx]
	if agenty < 100:
		knownmap[agenty + 1][agentx] = map[agenty + 1][agentx]
	path = []
	while agentx != xgoal or agenty != ygoal:
		#check nodes around
		opened = []
		heapq.heappush(opened, node(ygoal, xgoal, 0, None))
		closed = [[False for i in range(0, 101)] for j in range(0,101)]
		treepath = astar()
		if treepath == None:
			print("Path unreachable")
			sys.exit()
		while treepath.parent != None:
			knownmap[agenty][agentx] = map[agenty][agentx]
			if agentx > 0:
				knownmap[agenty][agentx - 1] = map[agenty][agentx - 1]
			if agentx < 100:
				knownmap[agenty][agentx + 1] = map[agenty][agentx + 1]
			if agenty > 0:
				knownmap[agenty - 1][agentx] = map[agenty - 1][agentx]
			if agenty < 100:
				knownmap[agenty + 1][agentx] = map[agenty + 1][agentx]
			if knownmap[treepath.parent.y][treepath.parent.x] == 'X':
				break
			#check for backtracking
			if (treepath.parent.x, treepath.parent.y) in path:
				path = path[0: path.index((treepath.parent.x, treepath.parent.y))]
			#check neighbors of child to see if shorter path can be drawn excluding parent
			if (treepath.parent.x + 1, treepath.parent.y) in path:
				path = path[0: path.index((treepath.parent.x + 1, treepath.parent.y)) + 1]				
			if (treepath.parent.x - 1, treepath.parent.y) in path:
				path = path[0: path.index((treepath.parent.x - 1, treepath.parent.y)) + 1]	
			if (treepath.parent.x, treepath.parent.y + 1) in path:
				path = path[0: path.index((treepath.parent.x, treepath.parent.y + 1)) + 1]	
			if (treepath.parent.x, treepath.parent.y - 1) in path:	
				path = path[0: path.index((treepath.parent.x, treepath.parent.y - 1)) + 1]			 
			path.append((treepath.parent.x, treepath.parent.y))
			agentx = treepath.parent.x
			agenty = treepath.parent.y
			treepath = treepath.parent
				
	for tup in path:
		map[tup[1]][tup[0]] = '@'
	map[ygoal][xgoal] = 'G'
	map[ystart][xstart] = 'S'
	with open('./maps/' + sys.argv[1] + 'blargeg', 'w+') as file:
		for line in map:
			for char in line:
				file.write(char + ' ')
			file.write('\n')
	with open('./results', 'a+') as file:
		file.write('Nodes opened: ' + str(acounter) + ' | Path length: ' + str(len(path)) + ' | Program: ' + str(sys.argv[0]) + 'Map: ' + sys.argv[1] + '\n')
	
