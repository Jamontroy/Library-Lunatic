from __future__ import annotations

import random

from .books import Book
from .draw import Renderer
from .palette import BOOK_TYPES, COLORS
from .player import Player
from .bookshelves import Bookshelves
from .collisions import Collisions
from .hud import HUD

import pygame

class Game:
    fps = 60

    SCREEN_W, SCREEN_H = 600, 800 
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
        self.state = "start"  # for lose screen
        self.bspawn_timer = 0.0 # timer that tracks time in between book spawning times
        self.hud = HUD(self.screen, self.SCREEN_W) # added for hud
        self.collisions = Collisions()
        self.carrying = 0
        self.books = pygame.sprite.Group() # to track books
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.state == "gameover" or "start":
                self.state = "playing"
                self.timer = 60.0
                self.carrying = 0
                self.books.empty()
                self.player = Player(self.SCREEN_W, self.SCREEN_H)
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False


    def update(self, dt: float) -> None:
        if self.state == "gameover":
            return
        if self.state == "playing":
            self.player.update(dt)
            self.carrying = len(self.player.bookscarried) # uses the length of the list of books to see how many are carried
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.state = "gameover"
            self.bspawn_timer += dt #
            if self.bspawn_timer >= 5:
                self.try_book_spawn()
                self.bspawn_timer = 0.0
            self.player.score += self.collisions.update(self.player, self.bookshelves, self.books, self.hud)

    '''
     I added this as a simple book spawner, however this definitely can change later depending on
    how we choose to implement book spawning conditions (conveyor belt, patrons dropping, etc.)
    '''
    def try_book_spawn(self) -> None:
        x = random.randint(0, self.SCREEN_W)
        y = random.randint(0, self.SCREEN_H)
        t = random.choice(list(BOOK_TYPES.keys()))
        new_book = Book(center =(x, y), tag = (t))
        while self.collisions.book_bs_col(new_book, self.bookshelves):
            x = random.randint(0, self.SCREEN_W)
            y = random.randint(0, self.SCREEN_H)
            new_book.rect.center = (x, y)
        self.books.add(new_book)


    def draw(self)-> None:
        self.renderer.draw_game(self.player, self.bookshelves)
        # Draw the HUD with the current timer score and number of books being carried
        for book in self.books: # draws books on screen
            book.draw(self.screen)
        self.hud.draw(self.timer, self.player.score, self.carrying) #0 is a placeholder for carrying for now
        # Draw game over screen on top of everything
        if self.state == "gameover":
            overlay = pygame.Surface((self.SCREEN_W, self.SCREEN_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))
            big_font = pygame.font.SysFont(None, 64)
            small_font = pygame.font.SysFont(None, 32)
            s = big_font.render("Game Over!", True, COLORS.text)
            self.screen.blit(s, (self.SCREEN_W // 2 - s.get_width() // 2, self.SCREEN_H // 2 - 40))
            r = small_font.render("Press Space to play again", True, COLORS.subtle)
            self.screen.blit(r, (self.SCREEN_W // 2 - r.get_width() // 2, self.SCREEN_H // 2 + 20))
        if self.state == "start":
            overlay = pygame.Surface((self.SCREEN_W, self.SCREEN_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))
            big_font = pygame.font.SysFont(None, 64)
            small_font = pygame.font.SysFont(None, 32)
            s = big_font.render("Library Lunatic", True, COLORS.text)
            self.screen.blit(s, (self.SCREEN_W // 2 - s.get_width() // 2, self.SCREEN_H // 2 - 40))
            r = small_font.render("Collect books and take them to their shelves", True, COLORS.subtle)
            self.screen.blit(r, (self.SCREEN_W // 2 - r.get_width() // 2, self.SCREEN_H // 2 + 20))
            r = small_font.render("Press Space to Begin", True, COLORS.subtle)
            self.screen.blit(r, (self.SCREEN_W // 2 - r.get_width() // 2, self.SCREEN_H // 2 + 80))
            r = small_font.render("Control with WASD or ARROW keys", True, COLORS.subtle)
            self.screen.blit(r, (self.SCREEN_W // 2 - r.get_width() // 2, self.SCREEN_H // 2 + 120))

