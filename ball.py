import pygame

from vector import *

balls = []

class Ball:
    def __init__(self, x, y, radius, color, velocity):
        self.pos = Vector2d(x, y)
        self.radius = radius
        self.color = color
        self.velocity = velocity

        self.rect = pygame.Rect((self.pos.x - self.radius, self.pos.y - self.radius), (self.radius * 2, self.radius * 2))
        balls.append(self)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)
        pygame.draw.rect(screen, "green", self.rect, 1)

    def move(self, dt):
        self.pos += Vector2d(self.velocity.x * dt, self.velocity.y * dt)
        self.rect = pygame.Rect((self.pos.x - self.radius, self.pos.y - self.radius),
                                (self.radius * 2, self.radius * 2))
