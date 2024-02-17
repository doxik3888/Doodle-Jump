import pygame
import os
from scripts.constants import display_size
from scripts.player import Player
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.platform import Platform
from scripts.platform_generator import PlatformGenerator

class Game():
    def __init__(self) -> None:
        self.background_image = load_image('assets','images', 'background.png')
        self.platform_generator = PlatformGenerator(200)
        self.offset_y = 0
        
        self.player = Player((200, 200), load_image('assets', 'images', 'player.png'),5,20,0.65)

        self.platforms = list
        self.platforms = [ 
            Platform((240, 700), load_image("assets", "images", "platform.png")),
            Platform((100, 500), load_image("assets", "images", "platform.png")),
            Platform((400, 300), load_image("assets", "images", "platform.png")),
        ]

        self.losed = False
        self.font = pygame.Font(os.path.join('assets','fonts','pixel.ttf'),32)

        self.jump_sound =  pygame.mixer.Sound(
            os.path.join('assets','sounds','jump.mp3')
        )

        self.fallig_sound =  pygame.mixer.Sound(
            os.path.join('assets','sounds','falling.mp3')
        )

        self.breaking_sound = pygame.mixer.Sound(
            os.path.join('assets','sounds','platform-break.mp3')
        )

        pygame.mixer.music.load(os.path.join('assets','music','caves.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
    def render(self, surface):

        surface.blit(self.background_image, (0, 0))
        for platform in self.platforms:
            platform.render(surface, self.offset_y)
        self.player.render(surface, self.offset_y)

        score = round (- self.offset_y / 10)
        
        if self.losed :
            score_text = self.font.render('Ваш рекорд:{score}',True, (1,1,1))
            hint_text = self.font.render('Нажми на любую клавишу', True,(1,1,1))

            score_rect = score_text.get_rect(
                centerx = display_size[0]/2,
                centery = display_size[1]/2 + 25
            )
            hint_rect = hint_text.get_rect(
                centerx = display_size[0]/2,
                centery = display_size[1]/2 + 25
            )

            surface.blit(score_text,score_rect)
            surface.blit(hint_text,hint_rect)

        else :
            text = self.font.render(str(score),True, (1,1,1))
            rect = text.get_rect(midtop=(display_size[0]/2, 10))
            surface.blit(text,rect)

    def restart(self):
        self.player.reset((240,600))
        self.losed = False
        self.offset_y = 0
        self.platforms = list()
        self.platform_generator.create_start_configuration()

    def handle_key_down_event(self, key):
        if self.losed:
            self.restart()
         

        elif key == pygame.K_a:
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True
    def handle_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        elif key == pygame.K_d:
            self.player.is_walking_right = False

    def handle_create_platform_event(self,platform):
        self.platforms.append(platform)

    def update(self):
        self.losed = self.player.rect.top - self.offset_y >= display_size[1]
        if self.platforms:
            self.platform_generator.update(self.offset_y, self.platforms)

        if self.losed:
            return        
        self.player.update()
        for platform in self.platforms.copy():
            platform.update()
            if self.player.collide_sprite(platform):
                self.player.on_platform = True

                if platform.type == 'BreakingPlatsorm':
                    self.platforms.remove(platform)
                elif platform.type == 'DisappearingPlatform':
                    platform.player_touched = True

            if (platform.type == 'DisappearingPlatform'
                and platform.disapperance_time <= 0 ):
                self.platforms.remove(platform)

        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
