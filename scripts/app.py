import pygame
import os
from scripts.game import Game
class App:
    def __init__(self) :
        self.display_size = (480, 720)
        self.running = True
        self.maxFPS = 60

        self.display = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()
        self.game = Game()

        pygame.display.set_caption('Doodle Jump')
        pygame.display.set_icon(pygame.image.load(os.path.join("assets","icons","icon.ico")))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.display.fill((0,0,0))
        self.game.render(self.display)
        pygame.display.update()

    def run(self):
        while self.running:
            self.hundle_events()
            self.upgrate()
            self.render()

            self.clock.tick(self.maxFPS)