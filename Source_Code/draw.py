import pygame
from .palette import COLORS
from .player import Player

class Renderer:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw_game(self, player: Player) -> None:
        self.screen.fill(COLORS.bg)
        player.draw(self.screen)