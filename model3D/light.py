#application internal imports
from algebra import Vector
from algebra import Point
import conf

class Light(object):
	lp = None	#light position Point(x, y, v)
	ka = None	#ka - ambiental reflection
	Ia = None	#Ia - Environmental color vector
	kd = None	#kd - Diffuse constant
	Od = None	#Od - Diffuse vector
	ks = None	#ks - Specular
	Il = None	#Il - Light source color
	n = None	#n  - Roughness constant

	def __init__(self):
		#load informations from file
		cl_file = open(conf.illumination, "r")

		print("from file:" + conf.illumination)
		print("\tloaded lights settings...")

		#loading light position (world coordinate)
		line = cl_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.pos = Point(x, float(line[n1:n2]), float(line[n2+1:]))

		#ka loading
		self.ka = float(cl_file.readline())

		#Ia loading
		line = cl_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.Ia = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

		#kd loading
		self.kd = float(cl_file.readline())

		#Od loading
		line = cl_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.Od = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

		#ks loading
		self.ks = float(cl_file.readline())

		#Il loading
		line = cl_file.readline()
		n1 = line.find(" ")
		x = float(line[:n1])
		n2 = n1 + line[n1+1:].find(" ") + 1
		self.Il = Vector(x, float(line[n1:n2]), float(line[n2+1:]))

		#n loading
		self.n = float(cl_file.readline())

		print("loaded\n")
		cl_file.close()

	#debugging methods
	def print(self):
		print("Light:")
		print("\tlight point: " + str(self.lp))
		print("\tambiental reflection: " + str(self.ka))
		print("\tEnvironmental color vector: " + str(self.Ia))
		print("\tDiffuse constant: " + str(self.kd))
		print("\tDiffuse vector: " + str(self.Od))
		print("\tSpecular: " + str(self.ks))
		print("\tLight source color: " + str(self.Il))
		print("\tRoughness constant: " + str(self.n))
		print("\n")

# luminacao.txt
# /---------------------------------------\
# | -200 -50 300                          | ; Pl - Posicao da luz em coordenadas de mundo
# | 1                                     | ; ka - reflexao ambiental
# | 2 2 2                                 | ; Ia - vetor cor ambiental
# | 1                                     | ; kd - constante difusa
# | 1 1 1                                 | ; Od - vetor difuso
# | 0.5                                   | ; ks - parte especular
# | 0 255 0                               | ; Il - cor da fonte de luz
# | 2                                     | ; n  - constante de rugosidade
# |                                       |
# \---------------------------------------/
