class Sprite:
    def __init__(self, center, image):
        self.image = image.copy()
        self.rect= self.image.get_frect()
        self.rect.center = center

    def render(self,surface):
        surface.blit(self.image,self.rect)
