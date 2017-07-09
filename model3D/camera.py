#external libraries imports
import pygame
from pygame.locals import *

#internal packege imports
from model3D import Model

#application internal imports
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
	display = None #pygame display
	screen = None #pygame surface

	def __init__(self, model):
		self.mdl = model

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

	def set(self, width, height):
		self.display = (800, 600)
		self.screen = pygame.display.set_mode(self.display)

	def orthogonalize(self):
		###
		# find a v_U orthogonal to v_V and v_N
		#see in: https://www.khanacademy.org/math/linear-algebra/alternate-bases/change-of-basis/v/linear-algebra-change-of-basis-matrix
		#and in: http://ccsubs.com/video/yt%3ArHonltF77zI/the-gram-schmidt-process-alternate-coordinate-systems-bases-linear-algebra-khan-academy/subtitles
		###

		#v1 = self.v_N
		#v2 = self.v_V
		#u2 = self.v_U
		u1 = self.v_V
		self.v_V = (self.v_V - self.v_N.projection(self.v_V)).normalize()
		self.v_U = self.v_N.crossProd(self.v_V)

	def draw(self):
		#printing edges
		if conf.settings["edges"]:
			for triangle in self.mdl.surfaces:
				for vertex in triangle:
					self.screen.set_at((int(self.mdl.vertices[vertex].x), int(self.mdl.vertices[vertex].y)), Color(255, 255, 255, 0))

	#debugging methods
	def print(self):
		print("Camera:")
		print("\tposition at" + str(self.pos))
		print("\tvector N " + str(self.v_N))
		print("\tvector V " + str(self.v_V))
		print("\tvector U " + str(self.v_U))
		print("\td " + str(self.d))
		print("\th " + str(self.h))
		print("\thas a model? " + str(self.mdl is not None))
		if self.display is None:
			print("\thas display? False")
		else:
			print("\thas display? " + str(self.display))
		print("\thas screen? " + str(self.screen is not None))
		print("\n")
