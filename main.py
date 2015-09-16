import pygame
from math import pi, cos, sin

# Some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BROWN = (179,169,141)

# key press event numbers
UP = 273
DOWN = 274
LEFT = 275
RIGHT = 276

rocket_vertices = ((-1,-1),(0,1),(1,-1),(-1,-1),(-0.5,-1.25),(0,-1),(0.5,-1.25),(1,-1))

def transform(vertices, center, orient, scale):
	screen = []
	for v in vertices:
		r = scale*(cos(orient+pi)*v[0] - sin(orient+pi)*v[1]) + center[0]
		c = scale*(sin(orient+pi)*v[0] + cos(orient+pi)*v[1]) + center[1]
		screen.append((r,c))

	return screen

def draw_rocket(surf, center, orient, scale):
	pygame.draw.polygon(surf, BLACK, transform(rocket_vertices, center, orient, scale), 1)

if __name__ == "__main__":

	pygame.init()
	size = (800, 600)
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Cool Canyon")
	
 	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	center = [400,300]
	orient = 0
	scale = 20
	speed = 0
	
	while not done:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					orient += -0.05
				if event.key == pygame.K_RIGHT:
					orient += 0.05
				if event.key == pygame.K_DOWN:
					speed += 1
				if event.key == pygame.K_UP:
					speed -= 1

					
		# --- Game logic should go here

		center[0] += speed*cos(orient+pi/2)
		center[1] += speed*sin(orient+pi/2)

		screen.fill(WHITE)
				
		# --- Drawing code should go here
		draw_rocket(screen, center, orient, scale)
		
		pygame.display.flip()
		
		clock.tick(60)
																		
