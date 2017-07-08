class Point:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "p (" + str(self.x) + ", " + str(self.y) + str(self.z) + ")"


class Vector:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "v (" + str(self.x) + ", " + str(self.y) + str(self.z) + ")"
