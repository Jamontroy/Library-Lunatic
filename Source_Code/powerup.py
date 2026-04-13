import pygame
from .palette import COLORS

class Powerup(pygame.sprite.Sprite):
    SIZE = 20

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center
        self.color = pygame.Color("#00BFFF")  # bright blue so it stands out

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, pygame.Color("#000000"), self.rect, 2)
        # draw a small "E" on it so the player knows its an energy drink
        font = pygame.font.SysFont(None, 18)
        label = font.render("E", True, pygame.Color("#000000"))
        surface.blit(label, (self.rect.x + 6, self.rect.y + 3))