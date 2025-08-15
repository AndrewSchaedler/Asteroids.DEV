import random
import pygame
from circleshape import CircleShape 
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Moves asteroid in straight line
        self.position += self.velocity * dt

    def split(self):
        # 1. Remove this asteroid
        self.kill()
        # 2. If too small, stop
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # 3. Pick a random split angle between 20° and 50°
        random_angle = random.uniform(20, 50)
        # 4. Create two new velocity vectors rotated in opposite directions
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        # 5. New radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # 6. Spawn first asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        # 7. Spawn second asteroid
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 * 1.2
        # 8. Add them to the same groups as the original asteroid
        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)