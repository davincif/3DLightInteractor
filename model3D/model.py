from algebra import Point
import conf

class Model:
	vertices = None #(x, y, z)
	vtc_qtd = 0
	edges = None #((v1), (v2))
	edg_qtd = 0
	surfaces = None #((v1), (v2), (v3))
	sfc_qtd = 0

	def __init__(self):
		#load informations from file
		co_file = open(conf.objects, "r")
		print("from file:" + conf.objects)

		#get quantities
		line = co_file.readline()
		n = line.find(" ")
		self.vtc_qtd = int(line[:n])
		if(conf.settings["edges"] == True):
			self.edg_qtd = int(line[n+1:])
		if(conf.settings["surfaces"] == True):
			self.sfc_qtd = int(line[n+1:])


		#get points
		print("\tloading points...")
		auxl = []
		for count in range(0, self.vtc_qtd):
			line = co_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			auxl.append( (x, float(line[n1:n2]), float(line[n2+1:])) )
		self.vertices = tuple(auxl)
		print("\t" + str(self.vtc_qtd) + " vertices loaded")

		#get triangles
		print("\n\tloading triangles...")
		auxl = []
		auxs = []
		for count in range(0, self.edg_qtd):
			line = co_file.readline()
			if(conf.settings["isply"] == True):
					line = line[line.find(" ")+1:]
			n1 = line.find(" ")
			x = int(line[:n1]) - 1
			n2 = n1 + line[n1+1:].find(" ") + 1
			y = int(line[n1:n2]) - 1
			z = int(line[n2+1:]) - 1

			if(conf.settings["edges"] == True):
				auxl.append( (x, y) )
				auxl.append( (y, z) )
			
			if(conf.settings["surfaces"] == True):
				auxs.append( (x, y, z) )

		if(conf.settings["edges"] == True):
			self.edges = tuple(auxl)

		if(conf.settings["surfaces"] == True):
			self.surfaces = tuple(auxs)

		print("\t" + str(self.edg_qtd) + " edges loaded")

		print("loaded\n")
		co_file.close()

	def draw(self):
	###
	# draw the model in the OpenGL
	###
		pass
