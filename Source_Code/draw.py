import pygame

from . import books
from .palette import COLORS
from .player import Player
from .bookshelves import Bookshelves, SCREEN_W, SCREEN_H

class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        backdrop = pygame.image.load("Assets/setting.png").convert()
        self.backdrop = pygame.transform.scale(backdrop, (SCREEN_W, SCREEN_H))

    def draw_game(self, player: Player, bookshelves: Bookshelves) -> None:
        self.screen.blit(self.backdrop, (0, 0))
        player.draw(self.screen)
        bookshelves.draw(self.screen)