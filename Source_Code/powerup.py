import pygame
from .palette import COLORS

class Powerup(pygame.sprite.Sprite):
    SIZE = 40

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center
        self.SpeedBoots = pygame.transform.scale2x(pygame.image.load(f"Assets/SpeedBoots.png").convert_alpha())

    def draw(self, surface):
        surface.blit(self.SpeedBoots, self.rect)

# Bookmark powerup (Thats just what i thought of we can change it): doubles the players score for a short time when picked up        
class Bookmark(pygame.sprite.Sprite):
    SIZE = 40

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center
        self.x2 = pygame.transform.scale2x(pygame.image.load(f"Assets/X2.png").convert_alpha())

    def draw(self, surface):
        surface.blit(self.x2, self.rect)

# Hourglass powerup: freezes the timer for a short time when picked up (Maybe we cant make it freeze hazzard later on)
class Hourglass(pygame.sprite.Sprite):
    SIZE = 40

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center
        self.hourglass = pygame.transform.scale2x(pygame.image.load(f"Assets/Hourglass.png").convert_alpha())

    def draw(self, surface):
        surface.blit(self.hourglass, self.rect)