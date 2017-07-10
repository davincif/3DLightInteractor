#application internal imports
from algebra import ObjPoint
import conf

class Model:
	vertices = None #ObjPoint(x, y, z, N) - N = triangle normal
	vtc_qtd = 0
	surfaces = None #((vertex1), (vertex2), (vertex3))
	sfc_qtd = 0

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
		auxl = []
		for count in range(0, self.vtc_qtd):
			line = co_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			auxl.append( ObjPoint(x, float(line[n1:n2]), float(line[n2+1:])) )
		self.vertices = tuple(auxl)
		print("\t" + str(self.vtc_qtd) + " vertices loaded")


		#get triangles
		print("\n\tloading triangles...")
		auxl = []
		for count in range(0, self.sfc_qtd):
			line = co_file.readline()
			if(conf.settings["isply"] == True):
					line = line[line.find(" ")+1:]
			n1 = line.find(" ")
			x = int(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			auxl.append( (x, int(line[n1:n2]), int(line[n2+1:])) )

		self.surfaces = tuple(auxl)

		print("\t" + str(self.sfc_qtd) + " surfaces loaded")

		print("loaded\n")
		co_file.close()

	def change_base(self, v1, v2, v3):
	###
	# change the light's coordinate from world coord. to the camera coord.
	# see in: https://www.khanacademy.org/math/linear-algebra/alternate-bases/change-of-basis/v/linear-algebra-change-of-basis-matrix
	###
		for vertex in self.vertices:
			vertex.x = vertex.x*v1.x + vertex.y*v2.x + vertex.z*v3.x
			vertex.y = vertex.x*v1.y + vertex.y*v2.y + vertex.z*v3.y
			vertex.z = vertex.x*v1.z + vertex.y*v2.z + vertex.z*v3.z