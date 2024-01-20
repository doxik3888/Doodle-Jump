class Sprite:
    def __init__(self, center, image):
        self.image = image.copy()
        self.rect= self.image.get_frect()
        self.rect.center = center

    def render(self,surface):
        surface.blit(self.image,self.rect)

    def collide_sprite(self,other):
        return self.rect.colliderect(other.rect)
