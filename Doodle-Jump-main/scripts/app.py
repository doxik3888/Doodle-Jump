import pygame

from scripts.game import Game
from scripts.functions import load_image 
from scripts.constants import display_size

class App:
    def __init__(self):
        self.running = True
        self.maxFPS = 60

        self.display = pygame.display.set_mode(display_size)
        self.clock = pygame.time.Clock()
        self.game = Game()

        pygame.display.set_caption('Dodle Jump')
        pygame.display.set_icon(load_image('assets','icons','icon.ico'))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            
            elif event.type == pygame.KEYDOWN:
                self.game.handle_key_down_event(event.key)
            elif event.type == pygame.KEYUP:
                self.game.handle_key_up_event(event.key)

    def update(self):
        self.game.update()

    def render(self):
        self.display.fill((0,0,0))
        self.game.render(self.display)
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.maxFPS)
