from __future__ import annotations

import random

from .books import Book
from .draw import Renderer
from .palette import BOOK_TYPES, COLORS
from .player import Player
from .bookshelves import Bookshelves
from .collisions import Collisions
from .hud import HUD
from .powerup import Powerup, Bookmark, Hourglass
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
        self.powerups = pygame.sprite.Group()
        self.bookmarks = pygame.sprite.Group()
        self.hourglasses = pygame.sprite.Group()
        self.sfx_music = pygame.mixer.Sound("Audio/music.wav")
        self.sfx_music.set_volume(0.15)
    
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.state == "gameover" or self.state == "start":
                self.state = "playing"
                self.timer = 60.0
                self.carrying = 0
                self.books.empty()
                self.powerups.empty()
                self.bookmarks.empty()
                self.hourglasses.empty()
                self.hud.threebooks.clear()
                self.player = Player(self.SCREEN_W, self.SCREEN_H)
                self.sfx_music.play(-1)
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
            if self.player.freeze_timer <= 0:
                self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.sfx_music.stop()
                self.state = "gameover"
            self.bspawn_timer += dt #
            if self.bspawn_timer >= 3.00:
                self.try_book_spawn()
                self.try_powerup_spawn()
                self.try_bookmark_spawn()
                self.try_hourglass_spawn()
                self.bspawn_timer = 0.0

            for powerup in list(self.powerups): #speed boost
                if self.player.rect.colliderect(powerup.rect):
                    self.player.boost_timer = self.player.BOOST_DURATION
                    powerup.kill()

            for bookmark in list(self.bookmarks):#2x points
                if self.player.rect.colliderect(bookmark.rect):
                    self.player.score_boost_timer = self.player.SCORE_BOOST_DURATION
                    bookmark.kill()

            for hourglass in list(self.hourglasses):
                if self.player.rect.colliderect(hourglass.rect):
                    self.player.freeze_timer = self.player.FREEZE_DURATION
                    hourglass.kill()

            score_gained = self.collisions.update(self.player, self.bookshelves, self.books, self.hud)
            if self.player.score_boost_timer > 0:
                score_gained *= self.player.SCORE_MULTIPLIER
            self.player.score += score_gained  # was self.player.score += self.collisions.update before bookmark
            self.timer += score_gained * 2  # add 2 seconds for each book returned

    '''
     I added this as a simple book spawner, however this definitely can change later depending on
    how we choose to implement book spawning conditions (conveyor belt, patrons dropping, etc.)
    '''
    def try_book_spawn(self) -> None:
        BORDER = 70
        x = random.randint(BORDER, self.SCREEN_W - BORDER)
        y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
        t = random.choice(list(BOOK_TYPES.keys()))
        new_book = Book(center =(x, y), tag = (t))
        while self.collisions.book_bs_col(new_book, self.bookshelves):
            x = random.randint(BORDER, self.SCREEN_W - BORDER)
            y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
            new_book.rect.center = (x, y)
        self.books.add(new_book)

    def try_powerup_spawn(self) -> None:
        if len(self.powerups) > 0:  # only one powerup on screen at a time
            return
        if random.random() > 0.1:  # 20% chance to spawn when called
            return
        BORDER = 70
        x = random.randint(BORDER, self.SCREEN_W - BORDER)
        y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
        new_powerup = Powerup(center=(x, y))
        while self.collisions.book_bs_col(new_powerup, self.bookshelves):
            x = random.randint(BORDER, self.SCREEN_W - BORDER)
            y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
            new_powerup.rect.center = (x, y)
        self.powerups.add(new_powerup)
    
    def try_bookmark_spawn(self) -> None:
        if len(self.bookmarks) > 0:  # only one bookmark on screen at a time
            return
        if random.random() > 0.1:  # 15% chance to spawn when called
            return
        BORDER = 50
        x = random.randint(BORDER, self.SCREEN_W - BORDER)
        y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
        new_bookmark = Bookmark(center=(x, y))
        while self.collisions.book_bs_col(new_bookmark, self.bookshelves):
            x = random.randint(BORDER, self.SCREEN_W - BORDER)
            y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
            new_bookmark.rect.center = (x, y)
        self.bookmarks.add(new_bookmark)

    def try_hourglass_spawn(self) -> None:
        if len(self.hourglasses) > 0:  
            return
        if random.random() > 0.1:  # 15% chance to spawn when called
            return
        BORDER = 60
        x = random.randint(BORDER, self.SCREEN_W - BORDER)
        y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
        new_hourglass = Hourglass(center=(x, y))
        while self.collisions.book_bs_col(new_hourglass, self.bookshelves):
            x = random.randint(BORDER, self.SCREEN_W - BORDER)
            y = random.randint(BORDER + 80, self.SCREEN_H - BORDER)
            new_hourglass.rect.center = (x, y)
        self.hourglasses.add(new_hourglass)
    


    def draw(self)-> None:
        self.renderer.draw_game(self.player, self.bookshelves)
        # Draw the HUD with the current timer score and number of books being carried
        for book in self.books: # draws books on screen
            book.draw(self.screen)
        for powerup in self.powerups:
            powerup.draw(self.screen)
        for bookmark in self.bookmarks:
            bookmark.draw(self.screen)
        for hourglass in self.hourglasses:
            hourglass.draw(self.screen)
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

