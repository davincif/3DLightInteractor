#application internal imports
from algebra import Vector
from algebra import Point
from model3D.light import Light
from model3D.model import Model
from model3D.camera import Camera
import conf

class World():
	model = None # 3D model to be loaded
	cam = None # camera (thing that sees the world)
	lpl = [] #light points list
	lp_qtd = 0 #light points quantity
	win_size = None #(width, height)

	def __init__(self, win_size):
		self.win_size = win_size
		self.model = Model()
		self.lpl = self.__load_lights() #light point
		self.lp_qtd = len(self.lpl)
		self.cam = Camera(self.model, self.lpl)
		self.cam.set(self.win_size[0], self.win_size[1])

	#commum methods
	def world_to_camera_coord(self):
		print("change base to camera's coordinate...")

		print("\tchanging model's points")
		self.model.change_base(self.cam)

		print("\tchanging light's positions")
		for light in self.lpl:
			light.change_base(self.cam)

		print("done\n")

	#Internal use only methods
	def __load_lights(self):
		#load informations from file
		cl_file = open(conf.illumination, "r")

		print("from file:" + conf.illumination)
		print("\tloaded lights settings...")

		lights = []

		line = cl_file.readline()
		while line != "":
			#loading light position (world coordinate)
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			pos = Point(x, float(line[n1:n2]), float(line[n2+1:]))

			#ka loading
			ka = float(cl_file.readline())

			#Ia loading
			line = cl_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			Ia = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

			#kd loading
			kd = float(cl_file.readline())

			#Od loading
			line = cl_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			Od = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

			#ks loading
			ks = float(cl_file.readline())

			#Il loading
			line = cl_file.readline()
			n1 = line.find(" ")
			x = float(line[:n1])
			n2 = n1 + line[n1+1:].find(" ") + 1
			Il = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

			#n loading
			n = float(cl_file.readline())

			lights.append(Light(pos, ka, Ia, kd, Od, ks, Il, n))
			line = cl_file.readline()

		print(str(len(lights)) + " light(s) loaded\n")
		cl_file.close()

		return lights

	def project(self):
	###
	# preapare the world to be drawn
	###
		print("Projecting 3D points into 2D...")
		self.model.calc_screen_projection(self.cam)
		print("done")

	def draw(self):
	###
	# onde the model, camera and lights are loaded and set, the normals
	# are set, the 3Dpoints are projected into 2D. Draw the world.
	###
		if conf.settings["vertex"]:
			self.cam.draw_vertex()

	#debugging methods
	def print(self):
		pass
