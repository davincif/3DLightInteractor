#external libraries imports
import pygame
from pygame.locals import *

#internal packege imports
# from model3D import Model
# from model3D import Light

#application internal imports
import math
import algebra.pointNvector2D
from algebra.pointNvector import ObjPoint
from algebra import Vector
from algebra import Point
import conf
from model3D.zbuffer import ZBuffer

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
	zBuffer = None #zBuffer

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
		self.zBuffer = ZBuffer(800, 600)

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
			#2D Points
			p2d0 = self.mdl.vertices2D[triangle[0]]
			p2d1 = self.mdl.vertices2D[triangle[1]]
			p2d2 = self.mdl.vertices2D[triangle[2]]

			#3D Points
			p3d0 = self.mdl.vertices[triangle[0]]
			p3d1 = self.mdl.vertices[triangle[1]]
			p3d2 = self.mdl.vertices[triangle[2]]

			#Normals
			n0 = p3d0.N
			n1 = p3d1.N
			n2 = p3d2.N
			tup = max((p2d0 - p2d1).module(), (p2d0 - p2d2).module())
			if tup != 0:
				tup = 1 / tup
				t = 0
			elif tup == 0:
				t = 1
				tup = 1
			while t <= 1:
				tp0 = t*p2d0
				pa = tp0 + (1 - t)*p2d1
				pb = tp0 + (1 - t)*p2d2

				sup = (pa - pb).module()
				if sup != 0:
					sup = 1 / sup
					s = 0
				elif sup == 0:
					s = 1
					sup = 1
				while s <= 1:
					point = s*pa + (1 - s)*pb
					self.rast_aux(p2d0, p2d1, p2d2, point, triangle)
					s += sup
				self.rast_aux(p2d0, p2d1, p2d2, pa, triangle)
				t += tup
			self.rast_aux(p2d0, p2d1, p2d2, p2d0, triangle)

	def rast_aux(self, p2d0, p2d1, p2d2, point, triangle):
		alpha, beta, gama = self.baricentrica(p2d0, p2d1, p2d2, point)

		p03D = self.mdl.vertices[triangle[0]]
		p13D = self.mdl.vertices[triangle[1]]
		p23D = self.mdl.vertices[triangle[2]]
		point3D = (p03D * alpha) + (p13D * beta) + (p23D * gama)
		point3D.N = (p03D.N * alpha) + (p13D.N * beta) + (p23D.N * gama)
		if(self.zBuffer.compare_and_set(int(point.x), int(point.y), point3D.z)):
			#geeting phong
			vl = Vector(0, 0, 0) #vector light
			for light in self.lights:
				vl = vl + light.phong(point3D, self.pos)

			vl = vl + self.lights[0].get_ambiental_color()

			#light ceil
			#R
			if vl.x > 255:
				vl.x = 255
			elif vl.x < 0:
				vl.x = 0

			#G
			if vl.y > 255:
				vl.y = 255
			elif vl.y < 0:
				vl.y = 0

			#B
			if vl.z > 255:
				vl.z = 255
			elif vl.z < 0:
				vl.z = 0
			self.screen.set_at((int(point.x), int(point.y)), Color(int(vl.x), int(vl.y), int(vl.z), 0))

	def triangleArea(self, v1, v2, v3):
		a = math.hypot((v1.x - v2.x), (v1.y - v2.y))
		b = math.hypot((v2.x - v3.x), (v2.y - v3.y))
		c = math.hypot((v1.x - v3.x), (v1.y - v3.y))
		S = (a+b+c)/2
		A = abs(S - a)
		B = abs(S - b)
		C = abs(S - c)

		return math.sqrt(S * A * B * C)

	def baricentrica(self, P1, P2, P3, P):

		value = self.triangleArea(P1, P2, P3)
		if value == 0:
			return P1.x / P.x, 0, 0
		alpha = self.triangleArea(P, P2, P3) / value
		beta = self.triangleArea(P1, P, P3) / value
		gama = self.triangleArea(P1, P2, P) / value
		return alpha, beta, gama

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
