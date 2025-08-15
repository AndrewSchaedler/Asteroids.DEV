import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        for container in self.containers:
            container.add(self)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_MOVE_SPEED * dt
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot.velocity = direction
        


