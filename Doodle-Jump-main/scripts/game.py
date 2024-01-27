import pygame
import os
from scripts.constants import display_size
from scripts.player import Player
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.platform import Platform

class Game():
    def __init__(self) -> None:
        self.background_image = load_image('assets','images', 'background.png')
        self.offset_y = 0
        
        self.player = Player((200, 200), load_image('assets', 'images', 'player.png'),5,20,0.65)
        self.platforms = [ 
            Platform((240, 700), load_image("assets", "images", "platform.png")),
            Platform((100, 500), load_image("assets", "images", "platform.png")),
            Platform((400, 300), load_image("assets", "images", "platform.png")),
        ]
    def render(self, surface):
        surface.blit(self.background_image, (0, 0))
        for platform in self.platforms:
            platform.render(surface, self.offset_y)
        self.player.render(surface, self.offset_y)



    def handle_key_down_event(self, key):
        if key == pygame.K_a:
            self.player.is_walkind_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True
    def handle_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.is_walkind_left = False
        elif key == pygame.K_d:
            self.player.is_walking_right = False
    def update(self):
        self.player.update()
        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform = True
        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
