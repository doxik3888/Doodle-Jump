from scripts.platform import Platform
from scripts import load_image
from random import randint
from scripts.constants import display_size
from scripts.constants import CreatePlatformEvent
import pygame

class PlatformGenerator :
    def __init__(self,step) :
        self.step = step
        self.platform_images = [
            load_image('assets', 'image','platform.png'),        
            load_image('assets', 'image','breaking-platform.png'),    
            load_image('assets', 'image','platform.png'),    
            load_image('assets', 'image','moving-platform.png'),    
        ]

    def create_start_configuration(self):

        platform = Platform((display_size[0]/2, display_size[1]-50), self .platform_images[0])
        event =pygame.Event(CreatePlatformEvent,{'platform': platform})
        pygame.event.post(event)

        for y in ranger(int(display_size[1] / self.step), - 1,-1 ):
            self.create_platform(y * self.step)

    def create_platform(self, center_y):
        number = randint(0,3)
        image = self.platform_image[number]
        min_x = image.get_wigth()//2
        max_x = display_size[0] - image.get_width()//2
        center = (randint(min_x,max_x), center_y)

        event = pygame.Event(CreatePlatformEvent, {'platform': Platform(center, image)})
        pygame.event.post(event)

    def update(self,offset_y, platform):
        if platforms[- 1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms