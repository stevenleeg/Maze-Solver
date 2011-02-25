"""
Maze Solver 4.0
By Steve Gattuso

Based on:
http://ngattuso.googlepages.com/proj043.html
"""

class Maze:
	def __init__(self):
		self.maze = []
		self.size = ()
		self.start = ()
		self.finish = ()
	
	def __str__(self):
		ret = ""
		for line in self.maze:
			for char in line:
				ret += char
			ret += '\n'
		return ret
	
	def from_file(self, filename):
		# Get and parse the maze
		f = open(filename).readlines()

		self.size = (len(f[0]), len(f))
		
		for line in f:
			self.maze.append(list(line))
		
		# Scan for the starting point
		y = 0
		for line in self.maze:
			if "S" in line:
				x = line.index('S')
				break
			else:
				y += 1
		self.start = (x, y)
		
		# Scan for the finishing point
		y = 0
		for line in self.maze:
			if "F" in line:
				x = line.index('F')
				break
			else:
				y += 1
		self.finish = (x, y)
	
	def get(self, coord):
		return self.maze[coord[1]][coord[0]]
	
	def set(self, coord, val):
		self.maze[coord[1]][coord[0]] = val
	
	# Returns a list of coordinates around the current one
	"""
	DIRECTION:
	0: Up
	1: Right
	2: Down
	3: Left
	"""
	def scan(self, coord, return_coords = False):
		coords = []
		vals = []
		# Above
		coords.append((coord[0], coord[1] + 1))
		
		# Right
		coords.append((coord[0] +1 , coord[1]))
		
		# Down
		coords.append((coord[0], coord[1] - 1))
		
		# Left
		coords.append((coord[0] - 1, coord[1]))
		
		# Filter out any negatives and replace with Nones
		##coords = filter(lambda x: x[0] >= 0 and x[1] >= 0, coords)
		for coord in coords:
			if (coord[0] < 0) or (coord[1] < 0):
				coords[coords.index(coord)] = None
			if (coord[0] > self.size[0]) or (coord[1] > self.size[1]):
				coords[coords.index(coord)] = None
		
		if return_coords:
			return coords
		else:
			for coord in coords:
				if coord is None:
					vals.append(None)
				else:
					vals.append(self.get(coord))
			return vals
	
	def advance(self, coord, direction):
		if direction is 0:
			return (coord[0], coord[1] + 1)
		elif direction is 1:
			return (coord[0] +1 , coord[1])
		elif direction is 2:
			return (coord[0], coord[1] - 1)
		elif direction is 3:
			return (coord[0] - 1, coord[1])
	
	def quadrant(self, coord):
		"""
		Returns the quadrant that the given coordinate is in
		Reference:    4 | 3
		              -----
		              1 | 2
		"""
		midx = self.size[0] / 2.0
		midy = self.size[1] / 2.0
		
		if (coord[0] < midx) and (coord[1] < midy):
			return 1
		elif (coord[0] > midx) and (coord[1] < midy):
			return 2
		elif (coord[0] > midx) and (coord[1] > midy):
			return 3
		elif (coord[0] < midx) and (coord[1] > midy):
			return 4
	
	#
	# Maze generation functions
	#
	def from_blank(self, x, y):
		# Generate a blank maze with all wall
		self.maze = []
		self.size = (x - 1, y - 1)
		self.start = None
		self.finish = None
		
		for line in range(y):
			self.maze.append([])
			for char in range(x):
				self.maze[line].append('#')
			self.maze[line].append('\n')
		
	
	def debug(self):
		maze = ""
		for line in self.maze:
			for char in line:
				maze += char
		
		print(
		"""Maze:
		%s
		
		Size: %s
		Start Pt.: %s
		Finish Pt: %s
		""".replace("	", "") % (maze, self.size, self.start, self.finish))
		
if __name__ == "__main__":
	m = Maze()
	m.from_file('maze.txt')
	m.debug()
