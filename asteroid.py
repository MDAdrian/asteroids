
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius_of_smaller_asteroids = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius_of_smaller_asteroids)
        new_asteroid_1.velocity = v1 * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius_of_smaller_asteroids)
        new_asteroid_2.velocity = v2 * 1.2
