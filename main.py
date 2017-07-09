#standard python imports
import sys

#external libraries imports
import pygame
from pygame.locals import *

#application internal imports
from model3D import Model
from model3D import Camera

def version_check():
	#version checking
	if not sys.version_info > (3, 0):
		#wrong python interpreter
		print("PYTHON 3 REQUIRED")
		print("Quiting...\n")
		exit()
	elif not sys.version_info > (3, 2):
		#pygame requires python 3.2, and pyopengl, 3.3
		print("This version of PYTHON IS TOO OLD. Need 3.2 or higher")
		print("Quiting...\n")
		exit()

	print("version checked >> Python "
		+ str(sys.version_info[0]) + "."
		+ str(sys.version_info[1]) + "."
		+ str(sys.version_info[2]) + "\n")

def main():
	#set section
	version_check()

	model = Model()
	cam = Camera(model)

	#game init section
	pygame.init()
	display = (800, 600)
	screen = pygame.display.set_mode(display)

	xx = 1
	yy = 1
	#main loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		xx += 1
		yy += 1
		screen.set_at((xx, yy), Color(255, 255, 255, 0))
		# pygame.display.update() #it seems have problems
		pygame.display.flip()
		pygame.time.wait(10)



if __name__ == '__main__':
	main()
