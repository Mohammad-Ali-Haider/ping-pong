import pygame

from player import *
from ball import *
from rectangle import *

GAME_RES = (GAME_WIDTH, GAME_HEIGHT) = (700, 700)
GAME_BG = "black"
FPS = 60
PLAYER_LENGTH = 100

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(GAME_RES)
        self.clock = pygame.time.Clock()

    def draw(self, entities):
        self.screen.fill(GAME_BG)
        for entity in entities:
            entity.draw(self.screen)

        pygame.display.flip()

    def run(self):
        running = True

        Player(10, GAME_HEIGHT/2 - PLAYER_LENGTH/2, PLAYER_LENGTH, "left", 10, "white", pygame.K_w, pygame.K_s)
        Player(GAME_WIDTH - 15 - 10, GAME_HEIGHT/2 - PLAYER_LENGTH/2, PLAYER_LENGTH, "right", 10, "blue", pygame.K_UP, pygame.K_DOWN)
        Ball(GAME_WIDTH/2, GAME_HEIGHT/2, 10, "red", Vector2d(300, 0))

        Rectangle(0, 0, GAME_WIDTH, 30, "grey", "up")
        Rectangle(0, GAME_HEIGHT-30, GAME_WIDTH, 30, "grey", "down")


        while running:
            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            dt = self.clock.tick(FPS)/1000

            entities = players + balls + rectangles

            for player in players:
                player.move()
                for ball in balls:
                    player.collision(ball)

            for ball in balls:
                ball.move(dt)

            for rect in rectangles:
                for ball in balls:
                    rect.collision(ball)

            self.draw(entities)

if __name__ == '__main__':
    APP = App()
    APP.run()