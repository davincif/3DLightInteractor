#external libraries imports
import pygame
from pygame.locals import *

#internal packege imports
# from model3D import Model
# from model3D import Light

#application internal imports
import algebra.pointNvector2D
from algebra import Vector
from algebra import Point
import conf

class Camera:
	pos = None #posotion = Point(x, y, z)
	v_N = None #Vector N = Vector(x, y, z)
	v_V = None #Vector V = Vector(x, y, z)
	v_U = None #Vector orthogonal to N and V
	d = None #d
	h = None #(hx, hy)
	mdl = None #the model3D to be printed
	lights = None #a list of the lights presented on the cine
	display = None #pygame display (width, height)
	screen = None #pygame surface

	def __init__(self, model, lights):
		self.mdl = model
		self.lights = lights

		#load informations from file
		cc_file = open(conf.camera, "r")

		print("from file:" + conf.camera)
		print("\tloaded camera settings...")

		#loading camera position (world coordinate)
		line = cc_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.pos = Point(x, float(line[n1:n2]), float(line[n2+1:]))

		#loading vector N
		line = cc_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.v_N = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

		#loading vector V
		line = cc_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.v_V = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

		#loading d and h
		line = cc_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.d = x
		self.h = (float(line[n1:n2]), float(line[n2+1:]))

		print("loaded\n")
		cc_file.close()

		#create camera canonical base
		self.orthogonalize()


	#commum methods
	def set(self, width, height):
		self.display = (800, 600)
		self.screen = pygame.display.set_mode(self.display)

	def orthogonalize(self):
		###
		# find a v_U orthogonal to v_V and v_N
		# see in: http://planetmath.org/exampleofgramschmidtorthogonalization
		###

		#v1 = self.v_N
		#v2 = self.v_V
		#u2 = self.v_U
		u1 = self.v_V
		self.v_V = self.v_V - self.v_N.projection(self.v_V)
		self.v_V.normalize()
		self.v_U = self.v_N.crossProd(self.v_V)
		self.v_U.normalize()
		self.v_N.normalize()

	def draw_vertex(self):
		#printing the points of the object
		for point in self.mdl.vertices2D:
			self.screen.set_at((int(point.x), int(point.y)), Color(255, 255, 255, 0))

	def rasterization(self):
		for triangle in self.mdl.surfaces:
			p0 = self.mdl.vertices2D[triangle[0]]
			p1 = self.mdl.vertices2D[triangle[1]]
			p2 = self.mdl.vertices2D[triangle[2]]
			t = 0
			while t <= 1:
				tp0 = t*p0
				pa = tp0 + (1 - t)*p1 #baricentric
				pb = tp0 + (1 - t)*p2
				s = 0
				while s <= 1:
					point = s*pa + (1 - s)*pb
					self.screen.set_at((int(point.x), int(point.y)), Color(255, 255, 255, 0))
					s += 0.1
				t += 0.1

	def normalPointInversion(pos3D, N):
		aux = -pos3D.x * N.x + -pos3D.y * N.y + -pos3D.z * N.z
		if (aux < 0):
			return -N
		else:
			return N

	#debugging methods
	def print(self):
		print("Camera:")
		print("\tposition at: " + str(self.pos))
		print("\tvector N: " + str(self.v_N))
		print("\tvector V: " + str(self.v_V))
		print("\tvector U: " + str(self.v_U))
		print("\td " + str(self.d))
		print("\th " + str(self.h))
		print("\thas a model? " + str(self.mdl is not None))
		if self.display is None:
			print("\thas display? False")
		else:
			print("\thas display? " + str(self.display))
		print("\thas screen? " + str(self.screen is not None))
		print("\n")
