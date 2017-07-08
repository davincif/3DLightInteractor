import sys

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from model3D import Model
from model3D import Camera

def version_check():
	#version checking
	if not sys.version_info > (3, 0):
		#wrong python interpreter
		print("PYTHON 3 REQUIRED")
		print("Quiting...\n")
		exit()
	elif not sys.version_info > (3, 3):
		#pygame requires python 3.2, and pyopengl, 3.3
		print("This version of PYTHON IS TOO OLD. Need 3.3 or higher")
		print("Quiting...\n")
		exit()

	print("version checked")

def main():
	#set section
	version_check()
	print("\n")

	model = Model()
	cam = Camera()

	#game init section
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 800)
	cam.draw()

	#main loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		model.draw()
		# pygame.display.update() #it seems have problems
		pygame.display.flip()
		pygame.time.wait(10)



if __name__ == '__main__':
	main()
