import pygame
import random

from .palette import COLORS

BOOK_COLORS = [
    COLORS.book_red,
    COLORS.book_green,
    COLORS.book_blue,
    COLORS.book_yellow,
    COLORS.book_purple,
    COLORS.book_orange,
]

class Book:
    SIZE = 20

    def __init__(self, screen_w: int, screen_h: int) -> None:
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE*1.5)
        self.color = None
        self.active = True  # False once the book is picked up
        self.spawn()

    def spawn(self) -> None:
        # Place the book at the bottom center of the screen
        self.rect.centerx = self.screen_w // 2
        self.rect.bottom = self.screen_h - 20
        # Pick a random color from the list
        self.color = random.choice(BOOK_COLORS)
        self.active = True

    def draw(self, surface: pygame.Surface) -> None:
        if self.active:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=4)