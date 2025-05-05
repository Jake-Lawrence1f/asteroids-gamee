import pygame

from constants import *

def main():
	print("Starting Asteroids!") 

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	

		screen.fill("black")

		pygame.display.flip()

if __name__== "__main__":
	main()
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")



#this line ensures the main() fucntion is only called when this file is run directly; it won't
#run if it's imported as a module. it's considered the "pythonic" way to structure an
#executable program in python. Technically you could just call main()
