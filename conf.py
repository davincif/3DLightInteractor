#definitos pela monitoria
global camera
global illumination
global objects

#adicionados por mim
global show
global settled
global settings

settled = False

def init():
	print("making settings...")

	#using globals
	global camera
	global illumination
	global objects
	global settled
	global show
	global settings

	camera = "calice.cfg"
	illumination = "multi_iluminacao.txt"
	objects = "calice.byu"
	show = "settings"
	settings = {}

	prepath = "entry_files/"

	camera = prepath + camera
	illumination = prepath + illumination
	objects = prepath + objects
	show = prepath + show

	#read and set settings
	print("\tloading settings...")
	set_fiel = open(show, "r")
	lines = set_fiel.readlines()

	for line in lines:
		line = line.strip().replace(" ", "")
		n = line.find("=")
		command = line[:n]
		status = line[n+1:]
		settings[command] = status.lower() == "true"

	print("\t\t", settings)
	print("\tloaded")
	set_fiel.close()

	settled = True
	print("made\n")