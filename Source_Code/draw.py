import pygame
from .palette import COLORS
from .player import Player
from .bookshelves import Bookshelves
from .books import Book

class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw_game(self, player: Player, bookshelves: Bookshelves, book: Book) -> None:
        self.screen.fill(COLORS.bg)
        player.draw(self.screen)
        bookshelves.draw(self.screen)
        book.draw(self.screen)
        