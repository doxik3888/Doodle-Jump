from scripts.sprite import Sprite

class Player(Sprite):
    def __init__(self, center, image, speed, jump_power, gravity):
        super().__init__(center, image)

        self.jump_power = jump_power
        self.speed = speed
        self.gravity = gravity

        self.velocity_y = 0
        self.is_walking_right = False
        self.is_walking_left = False
        self.on_platform = False

    def update(self):

        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect += self.velocity_y
