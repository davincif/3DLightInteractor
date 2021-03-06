#standard python imports
import sys
import time

#external libraries imports
import pygame
from pygame.locals import *

#application internal imports
from world import World
import conf

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
	#setting time
	startTime = time.time()

	#set section
	version_check()
	conf.init()
	print("\n")

	#main variables crate
	world = World(win_size=(800, 600))
	world.world_to_camera_coord()
	world.project()

	#game init section
	pygame.init()

	world.draw()

	#time to render
	endTime = time.time()
	print("time to complete: " + str(endTime - startTime) + "s.")

	#main loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# pygame.display.update() #it seems have problems
		pygame.display.flip()
		# pygame.time.wait(10)



if __name__ == '__main__':
	main()
