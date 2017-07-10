#application internal imports
from model3D.model import Model
from model3D.camera import Camera
from model3D.light import Light

class World(object):
	model = None # 3D model to be loaded
	cam = None # camera (thing that sees the world)
	lpl = [] #light points list
	win_size = None #(width, height)

	def __init__(self, win_size):
		self.win_size = win_size
		self.model = Model()
		self.cam = Camera(self.model)
		self.lp = Light() #light point
		self.cam.set(self.win_size[0], self.win_size[1])
