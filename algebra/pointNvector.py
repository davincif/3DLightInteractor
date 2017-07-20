#standard python imports
import numbers
import math

class Point:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "p (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

	def __sub__(self, other):
		if isinstance(other, Point):
			return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ".")

	def __add__(self, other):
		if isinstance(other, Point):
			return Point(self.x + other.x, self.y + other.y, self.z + other.z)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ".")

	def __radd__(self, other):
		return self.__mul__(other)

	def __mul__(self, other):
		if isinstance(other, numbers.Number):
			return Point(self.x * other, self.y * other, self.z * other)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ".")

	def __rmul__(self, other):
		return self.__mul__(other)


class ObjPoint(Point):
	N = None #Normal (yes, a Vector)

	def __init__(self, x, y, z):
		super(ObjPoint, self).__init__(x, y, z)
		self.N = Vector(0, 0, 0)

	def __str__(self):
		return "op [(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ") " + str(self.N) + "]"

		
class Vector:
	x = 0
	y = 0
	z = 0

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	#DataModel Python Method
	def __str__(self):
		return "v (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

	def __sub__(self, other):
		if type(other) is Vector:
			return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
		elif isinstance(other, numbers.Number):
			return Vector(self.x - other, self.y - other, self.z - other)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __rsub__(self, other):
		return self.__sub__(other)

	def __add__(self, other):
		if type(other) is Vector:
			return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __radd__(self, other):
		return self.__add__(other)

	def __mul__(self, other):
		if isinstance(other, numbers.Number):
			return Vector(self.x * other, self.y * other, self.z * other)
		elif type(other) is Vector:
			return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
		else:
			raise Exception("cannot multiply " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __rmul__(self, other):
		return self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, numbers.Number):
			return Vector(self.x / other, self.y / other, self.z / other)
		else:
			raise Exception("cannot divide " + str(type(self)) + " by " + str(type(other)) + ".")

	def __pow__(self, other):
		if isinstance(other, numbers.Number):
			return Vector(self.x**other, self.y**other, self.z**other)
		else:
			raise Exception("cannot pow " + str(type(self)) + " by " + str(type(other)) + ".")

	def __neg__(self):
		self.x = -self.x
		self.y = -self.y
		self.z = -self.z

	#commum methods
	def module(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def normalize(self):
		module = math.sqrt(self.x**2 + self.y**2 + self.z**2)
		self.x = self.x / module
		self.y = self.y / module
		self.z = self.z / module

	def dotProd(self, other):
	###
	# the dot product <self, other>
	###
		return self.x*other.x + self.y*other.y + self.z*other.z

	def projection(self, v):
	###
	# projection of v in subspace self
	###
		return (self.dotProd(v) / self.dotProd(self)) * self

	def crossProd(self, other):
	###
	# the cross product (self X other)
	###
		return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
