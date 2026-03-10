from __future__ import annotations

from dataclasses import dataclass, field

from Source_Code.draw import draw_game

import pygame

class Game:
    fps = 60

    SCREEN_W, SCREEN_H = 900, 1200 
    HUD_H = 56
    PADDING = 12

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.font = pygame.font.SysFont(None, 22)
        self.big_font = pygame.font.SysFont(None, 40)

        self.screen_rect = pygame.Rect(0, 0, self.SCREEN_W, self.SCREEN_H)
        self.playfield = pygame.Rect(
            self.PADDING,
            self.HUD_H + self.PADDING,
            self.SCREEN_W - 2 * self.PADDING,
            self.SCREEN_H - self.HUD_H - 2 * self.PADDING,
        )
    
    def handle_event(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                self.running = False
    
    def update(self, dt: float):
        pass

    def draw(self):
        draw_game(self.screen)