import pygame
import os
from scripts.functions import load_image
from scripts.sprite import Sprite

class Game:
    def __init__(self):
        self.background = load_image("assets","images","background.png")
        self.player = Sprite((200,200),load_image('assets','images','player.png')) 

    def render(self,surface: pygame.Surface):
        surface.blit(self.background,(0,0))
        self.player.render(surface)
    