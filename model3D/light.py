class Light(object):
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
