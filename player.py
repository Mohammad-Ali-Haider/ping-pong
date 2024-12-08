import pygame.draw
import random

from vector import *
from main import *

players = []


class Player:
    def __init__(self, x, y, length, place, speed, color, up, down):
        self.pos = Vector2d(x, y)
        self.length = length
        self.place = place
        self.speed = speed
        self.color = color
        self.up = up
        self.down = down

        self.width = 15
        self.rect = pygame.Rect((self.pos.x, self.pos.y), (self.width, self.length))
        self.center = self.rect.center
        players.append(self)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "green", self.rect, 2)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.up] and not self.pos.y < 30:
            self.pos.y -= self.speed
        elif keys[self.down] and not self.pos.y + self.length + 30 > GAME_WIDTH:
            self.pos.y += self.speed

        self.rect = pygame.Rect((self.pos.x, self.pos.y), (self.width, self.length))
        self.center = self.rect.center

    def collision(self, other):
        if self.rect.colliderect(other.rect):
            random_f = (self.center[1] - other.pos.y)/(self.length/2)
            print(random_f)
            if self.place == "left":
                other.velocity = Vector2d(abs((1 - random_f)) , - random_f).normalize() * other.velocity.magnitude()
            elif self.place == "right":
                other.velocity = Vector2d(-1 * abs(1 - random_f) , - random_f).normalize() * other.velocity.magnitude()


