#standard python imports
import sys
import numbers
import math

class Point2D:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "p (" + str(self.x) + ", " + str(self.y) + ")"

	def __sub__(self, other):
		if isinstance(other, Point2D):
			return Vector2D(self.x - other.x, self.y - other.y)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ".")
		
class Vector2D:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	#DataModel Python Method
	def __str__(self):
		return "v (" + str(self.x) + ", " + str(self.y) + ", " + ")"

	def __sub__(self, other):
		if type(other) is Vector2D:
			return Vector2D(self.x - other.x, self.y - other.y)
		else:
			raise Exception("cannot subtract " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __rsub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		if isinstance(other, numbers.Number):
			return Vector2D(self.x * other, self.y * other)
		else:
			raise Exception("cannot multiply " + str(type(self)) + " by " + str(type(other)) + ", vise versa.")

	def __rmul__(self, other):
		return self.__mul__(other)

	def __truediv__(self, other):
		if isinstance(other, numbers.Number):
			return Vector2D(self.x / other, self.y / other)
		else:
			raise Exception("cannot divide " + str(type(self)) + " by " + str(type(other)) + ".")

	def __pow__(self, other):
		if isinstance(other, numbers.Number):
			return Vector2D(self.x**other, self.y**other)
		else:
			raise Exception("cannot pow " + str(type(self)) + " by " + str(type(other)) + ".")

	def __neg__(self):
		self.x = -self.x
		self.y = -self.y

	#commum methods
	def module(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		auxv = self / self.module()
		self.x = auxv.x
		self.y = auxv.y

	def dotProd(self, other):
	###
	# the dot product <self, other>
	###
		return self.x*other.x + self.y*other.y

	def projection(self, v):
	###
	# projection of v in subspace self
	###
		return (self.dotProd(v) / self.dotProd(self)) * self
