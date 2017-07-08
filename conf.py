#definitos pela monitoria
camera = "camera.cfg"
illumination = "iluminacao.txt"
objects = "objeto.byu"

#adicionados por mim
show = "settings"
settings = {}

prepath = "entry_files/"

camera = prepath + camera
illumination = prepath + illumination
objects = prepath + objects
show = prepath + show

#read and set settings
print("loading settings...")
set_fiel = open(show, "r")
lines = set_fiel.readlines()

for line in lines:
	line = line.rstrip().replace(" ", "")
	n = line.find("=")
	command = line[:n]
	status = line[n+1:]
	settings[command] = status.lower() == "true"

print("\t", settings)
print("loaded\n")
set_fiel.close()