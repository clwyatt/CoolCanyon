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

def draw_rocket(surf, center, orient, scale):
	pygame.draw.polygon(surf, BLACK, transform(rocket_vertices, center, orient, scale), 1)

if __name__ == "__main__":

	pygame.init()
	size = (800, 600)
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Cool Canyon")

	background = pygame.image.load('images/window.png')
	background_rect = background.get_rect()

	mothership = pygame.image.load('images/mothership.png')
	mothership_rect = mothership.get_rect()

	saucer = pygame.image.load('images/saucer.png')
	saucer_rect = saucer.get_rect()

	
 	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	dx = 0
	dy = 0
	
	while not done:

		screen.blit(background,background_rect)
		screen.blit(saucer,saucer_rect.move(100+dx,100+dy))
		#screen.blit(mothership,mothership_rect.move(300,50))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			#if event.type == pygame.KEYDOWN:
				#if event.key == pygame.K_DOWN:

				#if event.key == pygame.K_UP:
					
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_LEFT]:
			dx += 5
		if keys[pygame.K_RIGHT]:
			dx += -5
		if keys[pygame.K_UP]:
			dy += 5
		if keys[pygame.K_DOWN]:
			dy += -5
					
		# --- Game logic should go here
		   				
		pygame.display.flip()
		
		clock.tick(60)
																		
