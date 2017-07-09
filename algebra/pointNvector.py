#standard python imports
import sys
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
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, numbers.Number):
			return Vector(self.x * other, self.y * other, self.z * other)
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

	#commum methods
	def module(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def normalize(self):
		return self / self.module()

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
