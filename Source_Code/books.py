import pygame
from .palette import BOOK_TYPES

class Book(pygame.sprite.Sprite):
    # size of the book 
    SIZE = 20
    def __init__(self, center, tag):
        super().__init__()

        self.book_sprites = {
            "red":    [pygame.transform.scale2x(pygame.image.load(f"Assets/RedBook.png").convert_alpha())],
            "blue":  [pygame.transform.scale2x(pygame.image.load(f"Assets/BlueBook.png").convert_alpha())],
            "green":  [pygame.transform.scale2x(pygame.image.load(f"Assets/GreenBook.png").convert_alpha())],
            "yellow": [pygame.transform.scale2x(pygame.image.load(f"Assets/YellowBook.png").convert_alpha())],
            "purple":  [pygame.transform.scale2x(pygame.image.load(f"Assets/PurpleBook.png").convert_alpha())],
            "orange": [pygame.transform.scale2x(pygame.image.load(f"Assets/OrangeBook.png").convert_alpha())],
        }

        # tag is the color of the book e.g. "red", "blue"
        # it needs to match a shelf tag to score a point
        self.tag = tag

        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center

    #Replaced the former system with colored rects for actual book sprite
    def draw(self, surface):
        surface.blit(self.book_sprites[self.tag][0], self.rect)