#application internal imports
from algebra import Point2D
from algebra import ObjPoint
import conf

class Model:
	vertices = [] #ObjPoint(x, y, z, N) - N = point normal
	vtc_qtd = 0
	surfaces = [] #((vertex1), (vertex2), (vertex3), N(x, y, z)) #N = triangle normal wich is a vector
	sfc_qtd = 0
	vertices2D = []

	def __init__(self):
		#load informations from file
		co_file = open(conf.objects, "r")
		print("from file:" + conf.objects)

		#get quantities
		line = co_file.readline()
		n = line.find(" ")
		self.vtc_qtd = int(line[:n])
		self.sfc_qtd = int(line[n+1:])

		#get points
		print("\tloading points...")
		for count in range(0, self.vtc_qtd):
			line = co_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			self.vertices.append( ObjPoint(x, float(line[n1:n2]), float(line[n2+1:])) )
		print("\t" + str(self.vtc_qtd) + " vertices loaded")

		#get triangles
		print("\n\tloading triangles...")
		for count in range(0, self.sfc_qtd):
			line = co_file.readline()
			if(conf.settings["isply"] == True):
					line = line[line.find(" ")+1:]
			n1 = line.find(" ")
			x = int(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			if(conf.settings["isply"] == True):
				self.surfaces.append( [x, int(line[n1:n2]), int(line[n2+1:]), None] )
			else:
				self.surfaces.append( [x - 1, int(line[n1:n2]) - 1, int(line[n2+1:]) - 1, None] )
		print("\t" + str(self.sfc_qtd) + " surfaces loaded")

		print("loaded\n")
		co_file.close()

		self.calc_triangles_normal()

	def calc_triangles_normal(self):
	###
	# calculate the normals of all triangles, but do not guarantee that
	# they will be all pointing in or out of the curve
	###
		print("calculating triangles' normal...")
		for triangle in self.surfaces:
			triangle[3] = (self.vertices[triangle[0]]-self.vertices[triangle[1]]).crossProd(self.vertices[triangle[2]]-self.vertices[triangle[1]])
			triangle[3].normalize()
		print("calculated\n")

	def change_base(self, v1, v2, v3):
	###
	# change the light's coordinate from world coord. to the camera coord.
	# see in: https://www.khanacademy.org/math/linear-algebra/alternate-bases/change-of-basis/v/linear-algebra-change-of-basis-matrix
	###
		for vertex in self.vertices:
			vertex.x = vertex.x*v1.x + vertex.y*v2.x + vertex.z*v3.x
			vertex.y = vertex.x*v1.y + vertex.y*v2.y + vertex.z*v3.y
			vertex.z = vertex.x*v1.z + vertex.y*v2.z + vertex.z*v3.z

	def calc_screen_projection(self, camera):
	###
	# project the 3D points the in screen, considering that they aready had their
	# base changed from the world's coordinate to the camera's one
	###
		dohx = camera.d / camera.h[0] #d over hx
		dohy = camera.d / camera.h[1] #d over hy
		for vertex in self.vertices:
			self.vertices2D.append(Point2D(dohx * (vertex.x / vertex.z), dohy * (vertex.y / vertex.z)))
			print(self.vertices2D[len(self.vertices2D) -1])
