import pygame.draw
from vector import *

rectangles = []
SHOW_HIT_BOXES = True
HIT_BOX_COLOR = "red"

FRICTION_CONSTANT = 1


class Rectangle:
    def __init__(self, x, y, width, length, color, place):
        self.pos = Vector2d(x, y)
        self.width = width
        self.length = length
        self.color = color
        self.place = place

        self.rect = pygame.Rect((self.pos.x, self.pos.y), (self.width, self.length))
        rectangles.append(self)

    def draw(self, screen):
        global SHOW_HIT_BOXES

        pygame.draw.rect(screen, self.color, self.rect)
        if SHOW_HIT_BOXES: pygame.draw.rect(screen, HIT_BOX_COLOR, self.rect, 2)

    def collision(self, other):
        if self.rect.colliderect(other.rect):
            if self.place == "up":
                other.velocity.y = abs(other.velocity.y)
            elif self.place == "down":
                other.velocity.y = -1 * abs(other.velocity.y)
