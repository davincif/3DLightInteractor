from OpenGL.GL import *
from OpenGL.GLU import *

from algebra import Point
import conf

class Model:
	vertices = None #(x, y, z)
	vtc_qtd = 0
	edges = None #((v1), (v2), (v3))
	edg_qtd = 0

	def __init__(self):
		#load informations from file
		co_file = open(conf.objects, "r")

		#get quantities
		line = co_file.readline()
		n = line.find(" ")
		vtc_qtd = int(line[:n])
		edg_qtd = int(line[n+1:])

		print("from file:" + conf.objects)

		#get points
		print("\tloading points...")
		auxl = []
		for count in range(0, vtc_qtd):
			line = co_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			auxl.append( (x, float(line[n1:n2]), float(line[n2+1:])) )
		self.vertices = tuple(auxl)
		print("\t" + str(vtc_qtd) + " vertices loaded")

		#get triangles
		print("\n\tloading triangles...")
		auxl = []
		for count in range(0, edg_qtd):
			line = co_file.readline()
			n1 = line.find(" ")
			x = int(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			auxl.append( (x - 1, int(line[n1:n2]) - 1, int(line[n2+1:]) - 1) )
			self.edges = tuple(auxl)
		print("\t" + str(edg_qtd) + " edges loaded")

		print("loaded\n")

		co_file.close()

	def draw(self):
		###
		# draw the model in the OpenGL
		###
		glBegin(GL_LINES) #GL_LINE_LOOP

		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.vertices[vertex])

		glEnd()
