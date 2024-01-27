import pygame 
import os

def load_image(*paths):
    path = os.path.join(*paths)
    image = pygame.image.load(path).convert()
    image.set_colorkey((0,0,0))

    return image