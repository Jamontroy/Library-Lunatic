from __future__ import annotations

from .draw import Renderer
from .player import Player
from .bookshelves import Bookshelves

import pygame

class Game:
    fps = 60

    SCREEN_W, SCREEN_H = 900, 1200 
    HUD_H = 56
    PADDING = 12

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))

        self.screen_rect = pygame.Rect(0, 0, self.SCREEN_W, self.SCREEN_H)
        self.running = True
        self.player = Player(self.SCREEN_W, self.SCREEN_H)
        self.bookshelves = Bookshelves()
        self.renderer = Renderer(self.screen)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
    
    def update(self, dt: float) -> None:
        self.player.update(dt)

    def draw(self)-> None:
        self.renderer.draw_game(self.player, self.bookshelves)