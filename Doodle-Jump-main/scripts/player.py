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
        if self.on_platform:
            self.velocity_y = - self.jump_power
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect += self.velocity_y

        if self.is_walking_right != self.is_walking_left:
            if self.is_walking_right:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        self.on_platform = False
