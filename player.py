import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
from circleshape import CircleShape

class Player(CircleShape):
    """__init__ is the special initialiser method in python. when you create an instance of a
    class, python automatically calls __init__ to set up the new object. that's why naming
    it player doesn't work as python won't recognise the constructor
    """
    def __init__(self, x, y, timer=0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt, shots_group):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(-dt)

        if keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot(shots_group)

        if self.timer > 0:
           self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots_group):
        if self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            shot_velocity = direction * PLAYER_SHOOT_SPEED
            new_shot = Shot(self.position.copy(), shot_velocity)
            shots_group.add(new_shot)








