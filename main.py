import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

if __name__ == "__main__":
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	dt = 0
	while running:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			running = False
		for updates in updatable:
			updates.update(dt)
		for asteroid in asteroids:
			if(asteroid.check_collisions(player)):
				print("Game over!")
				pygame.event.clear()
				exit() 
			for shot in shots:
				if(asteroid.check_collisions(shot)):
					shot.kill()
					asteroid.split()
		pygame.Surface.fill(screen, "black")
		for drawes in drawable:
			drawes.draw(screen)
		pygame.display.update()
		dt = clock.tick(60) / 1000
