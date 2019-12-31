from __future__ import print_function
import sys
import os
import random
import numpy

if __name__ == "__main__":
	if not os.path.exists('./maps/'):
    		os.mkdir('./maps/')
	for x in range(0, 50):
		f = open('./maps/map' + str(x), 'w+')
		map = [[numpy.random.choice(['_', 'X'], p=[.7, .3]) for i in range(0, 101)] for j in range(0, 101)]
		map[0][0] = 'S'
		map[100][100] = 'G'
		for line in map:
			for char in line:
				f.write(char + ' ')
			f.write('\n')
		f.close()
	
