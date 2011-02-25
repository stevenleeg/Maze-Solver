import sys
from random import randint, choice
from maze import Maze

# Start by creating a blank maze
# TODO: Input validation
maze= Maze()
maze.from_blank(int(sys.argv[1]), int(sys.argv[2]))

visited = []
path = []
current = (randint(0, maze.size[0]), randint(0, maze.size[1]))
while 1:
	visited.append(current)
	# Find which directions haven't been visited
	around = maze.scan(current, return_coords = True)
	not_visited = filter(lambda x: x not in visited, around)
	
	# Pick a random direction to proceed in that hasn't been visited
	try:
		direction = around.index(choice(not_visited))
	except IndexError:
		# Are we finished?
		if len(path) is 0:
			break
		# All directions have been visited, go back a space
		current = path[-1]
		path.remove(current)
		continue
	# Place a space as long as we're not on an edge
	if ((current[0] != 0) and (current[0] != maze.size[0])) and ((current[1] != 0) and (current[1] != maze.size[1])):
		maze.set(current, ' ')
	
	# Direction shit. I'm writing this at 12:44AM while listening to Radiohead - Sepeartor
	# Needless to say I have no fucking idea why it works...
	if (direction is 0) or (direction is 2):
		visited.append(around[1])
		visited.append(around[3])
	else:
		visited.append(around[0])
		visited.append(around[2])
	
	# Move on!
	path.append(current)
	current = maze.advance(current, direction)

# Now we need to place the start/finish points
# Find the midpoints
midX = maze.size[0] / 2
midY = maze.size[1] / 2

# Now let's find a point in the top left that's suitable
for y in range(midY):
	for x in range(midX):
		coord = (x, y)
		scan = maze.scan(coord)
		if scan.count('#') is 3 and scan.count(' ') is 1:
			maze.set(coord, 'S')
			maze.start = coord
			break
	if maze.start != None:
		break

# Now look for a finishing point in the bottom right
for y in range(midY):
	for x in range(midX):
		coord = (x + midX, y+midY)
		if scan.count('#') is 3 and scan.count(' ') is 1:
			maze.set(coord, 'F')
			maze.finish = coord
			break
	if maze.finish != None:
		break
maze.debug()
