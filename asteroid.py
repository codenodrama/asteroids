import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        old_radius = self.radius
        current_position = self.position
        old_velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_vector = old_velocity.rotate(random_angle)
        second_vector = old_velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(current_position[0], current_position[1], new_radius)
        first_asteroid.velocity = first_vector * 1.2
        second_asteroid = Asteroid(current_position[0], current_position[1], new_radius)
        second_asteroid.velocity = second_vector * 1.2