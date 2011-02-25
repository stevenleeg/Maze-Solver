"""
Maze Solver 4.0
By Steve Gattuso

Based on:
http://ngattuso.googlepages.com/proj043.html
"""
from maze import Maze
import sys

"""
For reference:
DIRECTION
0 - Above
1 - Right
2 - Down
3 - Left
"""


# LET'S DO IT!
maze = Maze()
maze.from_file(sys.argv[1])

current = maze.start

solved = False
while solved is False:
	# Scan around us
	around = maze.scan(current)
	
	# First, let's see if we're finished with the maze
	try:
		finish = around.index('F')
		# Mark off the last breadcrumb
		maze.set(current, '.')
		solved = True
		break
	except ValueError:
		pass
	
	# Guess not, let's go on
	try:
		direction = around.index(' ')
		# Place a breadcrumb and move forward one space in that direction
		if maze.get(current) != 'S':
			maze.set(current, '.')
		current = maze.advance(current, direction)
	except ValueError:
		# There's no space, so we're going to have to go back a space
		try:
			direction = around.index('.')
			# Place an explored breadcrumb and go back
			maze.set(current, '-')
			current = maze.advance(current, direction)
		except ValueError:
			print("Something went wrong! ", current)
			maze.debug()
			sys.exit(1)

mazec = ""
for line in maze.maze:
	for char in line:
		mazec += char.replace('-', ' ')
print("""Maze solved! Solution:
%s""" % mazec)
