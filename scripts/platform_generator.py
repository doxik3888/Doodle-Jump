from scripts.platform import Platform
from scripts.platform import BreakingPlatform
from scripts.platform import DisapperingPlatform
from scripts.platform import MovingPlatform
from scripts.functions import load_image
from random import randint
from scripts.constants import display_size
from scripts.constants import CreatePlatformEvent
import pygame

class PlatformGenerator :
    def __init__(self,step) :
        self.step = step
        self.platform_images = [
            load_image('assets', 'images','platform.png'),        
            load_image('assets', 'images','breaking-platform.png'),    
            load_image('assets', 'images','platform.png'),    
            load_image('assets', 'images','moving-platform.png'),    
        ]

    def create_start_configuration(self):

        platform = Platform((display_size[0]/2, display_size[1]-50), self .platform_images[0])
        event =pygame.Event(CreatePlatformEvent,{'platform': platform})
        pygame.event.post(event)

        for y in range(int(display_size[1] / self.step), - 1,-1 ):
            self.create_platform(y * self.step)

    def create_platform(self, center_y):
        number = randint(0,3)
        image = self.platform_images[number]
        min_x = image.get_width()//2
        max_x = display_size[0] - image.get_width()//2
        center = (randint(min_x,max_x), center_y)

        info= {'platform': Platform(center,image)}

        if number == 0:
            info = {'platform': Platform(center,image)}
        elif number == 1:
            info = {'platform': BreakingPlatform(center,image)}
        elif number == 2:
            info = {'platform': DisapperingPlatform(
                center,image, 180 + randint(0,100)
                )
            }
        else:
            info = {'platform': MovingPlatform(
                center,image,randint(100,300)/100)
            }

        event = pygame.Event(CreatePlatformEvent,info)

    def update(self,offset_y, platforms):
        if platforms[- 1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])