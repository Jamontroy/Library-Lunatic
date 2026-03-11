import pygame
from .palette import BOOK_TYPES

class Book(pygame.sprite.Sprite):
    # size of the book 
    SIZE = 20
    def __init__(self, center, tag):
        super().__init__()

        # tag is the color of the book e.g. "red", "blue"
        # it needs to match a shelf tag to score a point
        self.tag = tag

        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center

        # This is to get the book color from the palette
        # BOOK_TYPES["red"] returns (book_color, shelf_color) so we grab index 0
        book_color, shelf_color = BOOK_TYPES[tag]
        self.color = book_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=3)
        pygame.draw.rect(surface, pygame.Color("#000000"), self.rect, 2, border_radius=3)