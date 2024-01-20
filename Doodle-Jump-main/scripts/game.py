import pygame
import os
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.player import Player
from scripts.platform import Platform

class Game:
    def __init__(self):
        self.background = load_image("assets","images","background.png")
        self.player = Player((200,600),load_image('assets','images','player.png'),5, 20, 0.65 ) 
        self.platforms = [
            Platform((240, 700), load_image('assets', 'images', 'platform.png')),
            Platform((100, 450), load_image('assets', 'images', 'platform.png')),
            Platform((400, 200), load_image('assets', 'images', 'platform.png'))
        ]


    def render(self,surface: pygame.Surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.background_image, (0,0))

        for platform in self.platform:
            platform.render(surface)
        self.player.render(surface)
    
    def handle_key_down_event(self,key):
        if key == pygame.K_a :
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True
    def handle_key_up_event(self,key):
        if key == pygame.K_a :
            self.player.is_walking_left = False
        elif key == pygame.K_d:
            self.player.is_walking_right = False

    def update(self):
        self.player.update()
        
        for platform in self.platforms:
            if self.player.collide_sprite():
                self.player.on_platform = True