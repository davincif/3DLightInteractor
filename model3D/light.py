#application internal imports
from algebra import Vector

class Light():
	lp = None	#light position Point(x, y, v)
	ka = None	#ka - ambiental reflection
	Ia = None	#Ia - Environmental color vector
	kd = None	#kd - Diffuse constant
	Od = None	#Od - Diffuse vector
	ks = None	#ks - Specular
	Il = None	#Il - Light source color
	n = None	#n  - Roughness constant

	def __init__(self, pos, ka, Ia, kd, Od, ks, Il, n):
		self.lp = pos
		self.ka = ka
		self.Ia = Ia
		self.kd = kd
		self.Od = Od
		self.ks = ks
		self.Il = Il
		self.n = n

	#commum methods
	def change_base(self, camera):
	###
	# change the light's coordinate from world coord. to the camera coord.
	# see in: https://www.khanacademy.org/math/linear-algebra/alternate-bases/change-of-basis/v/linear-algebra-change-of-basis-matrix
	###
		self.lp.x = camera.v_U.x*(self.lp.x - camera.pos.x) + camera.v_V.x*(self.lp.y - camera.pos.y) + camera.v_N.x*(self.lp.z - camera.pos.z)
		self.lp.y = camera.v_U.y*(self.lp.x - camera.pos.x) + camera.v_V.y*(self.lp.y - camera.pos.y) + camera.v_N.y*(self.lp.z - camera.pos.z)
		self.lp.z = camera.v_U.z*(self.lp.x - camera.pos.x) + camera.v_V.z*(self.lp.y - camera.pos.y) + camera.v_N.z*(self.lp.z - camera.pos.z)

	def normalPointInversion(self, pos3D):
		# aux = -pos3D.x * pos3D.N.x + -pos3D.y * pos3D.N.y + -pos3D.z * pos3D.N.z
		V = Vector(-pos3D.x, -pos3D.y, -pos3D.z)
		V.normalize()
		if (pos3D.N.dotProd(V) < 0):
			return Vector(-pos3D.N.x, -pos3D.N.y, -pos3D.N.z)
		else:
			return pos3D.N

	def phong(self, point, campoint):
	###
	# receive a 3D point to mensure the light where point.N is the normal of the point
	# and the camera position
	# return a color Vector(R, G, B)
	###
		Ls = self.lp - point #The vector from the point toward the light source
		Ls.normalize()

		Vd = Vector(-campoint.x, -campoint.y, -campoint.z)  #viewer direction,the vector from the point toward the camera
		Vd.normalize()

		N = self.normalPointInversion(point)
		NdotLs = point.N.dotProd(Ls)
		if (NdotLs < 0):
			return Vector(0, 0, 0)
		else:
			Rm = (2 * NdotLs * point.N) - Ls #The direction that a perfectly reflected light ray takes when hits this point
			Rm.normalize()
			RprodV = Rm.dotProd(Vd)
			if (RprodV < 0):
				return N.dotProd(Ls) * self.kd * (self.Od*self.Il)
			else:
				return N.dotProd(Ls) * self.kd * (self.Od*self.Il) + RprodV **self.n * self.ks*self.Il

	def get_ambiental_color(self):
	###
	# returns the ambiental portion of the light
	###
		return self.ka*self.Ia

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
