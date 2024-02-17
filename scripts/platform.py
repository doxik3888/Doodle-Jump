from scripts.sprite import Sprite
from scripts.constants import display_size

class Platform(Sprite):
    type = "Platform"
    def update(self):
        pass

class MovingPlatform(Platform):
    type = "MovingPlatform"
    def __init__(self,center,image,speed):
        super().__init__(center,image)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0 :
            self.speed = abs(self.speed)
        if self.rect.right > display_size[0]:
            self.speed = -abs(self.speed)

class BreakingPlatform(Platform):
    type = 'BreakingPlatform'
    pass
    
class DisapperingPlatform(Platform):
    type = 'DisapperingPlatform'
    def __init__(self, center, image, disapperance_time):
        super().__init__(center, image)
        self.player_touched = False
        self.disapperance_start_time = disapperance_time
        self.disapperance_time = disapperance_time

    def update(self):
        if self.player_touched:
            self.disapperance_time -= 1
            mult = self.disapperance_time / self.disapperance_start_time
            self.image.set_alpha(int(255 * mult))