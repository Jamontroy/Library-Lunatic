from __future__ import annotations

from .draw import Renderer
from .player import Player
from .bookshelves import Bookshelves
from .hud import HUD

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
        self.timer = 60.0 # added for timer
        self.hud = HUD(self.screen, self.SCREEN_W) # added for hud
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
    
    def update(self, dt: float) -> None:
        self.player.update(dt)
        self.timer -= dt # added for timer

    def draw(self)-> None:
        self.renderer.draw_game(self.player, self.bookshelves)
        # Draw the HUD with the current timer score and number of books being carried
        self.hud.draw(self.timer, self.player.score, 0) #0 is a placeholder for carrying for now
