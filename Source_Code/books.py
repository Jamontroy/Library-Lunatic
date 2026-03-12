import pygame
import random

from .palette import COLORS

BOOK_COLORS = [
    COLORS.shelf_red,
    COLORS.shelf_green,
    COLORS.shelf_blue,
    COLORS.shelf_yellow,
    COLORS.shelf_purple,
    COLORS.shelf_orange,
]

class Book:
    SIZE = 10

    def __init__(self, screen_w: int, screen_h: int) -> None:
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE*1.5)
        self.color = None
        self.active = True
        self.spawn()

    def spawn(self) -> None:

        self.rect.centerx = self.screen_w // 2
        self.rect.bottom = self.screen_h - 20
        self.color = random.choice(BOOK_COLORS)
        self.active = True

    def draw(self, surface: pygame.Surface) -> None:
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect,)