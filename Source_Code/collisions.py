import pygame

from .player import Player
from .bookshelves import Bookshelves
from .books import Book
from .hud import HUD

class Collisions: 

    def __init__(self) -> None:
        self.sfx_bookDrop = pygame.mixer.Sound("Audio/BookDropOff.wav")
        self.sfx_bookDrop.set_volume(2)
        self.sfx_bookPickup = pygame.mixer.Sound("Audio/bookPickup.mp3")
        self.sfx_bookPickup.set_volume(0.5)
        self.sfx_ped_hit = pygame.mixer.Sound("Audio/bookPickup.mp3")
        self.sfx_ped_hit.set_volume(0.5)

    def player_shelf_col(self, player: pygame.Rect, bookshelf: pygame.Rect) -> None:
        if not player.rect.colliderect(bookshelf):
            return

        dx_left = player.rect.right - bookshelf.left
        dx_right = bookshelf.right - player.rect.left
        dy_top = player.rect.bottom - bookshelf.top
        dy_bottom = bookshelf.bottom - player.rect.top

        min_overlap = min(dx_left, dx_right, dy_top, dy_bottom)

        if min_overlap == dx_left:
            player.rect.right = bookshelf.left
            player.velocity.x = 0
        elif min_overlap == dx_right:
            player.rect.left = bookshelf.right
            player.velocity.x = 0
        elif min_overlap == dy_top:
            player.rect.bottom = bookshelf.top
            player.velocity.y = 0
        elif min_overlap == dy_bottom:
            player.rect.top = bookshelf.bottom
            player.velocity.y = 0

        player.pos.update(player.rect.center)


    '''
    this deals with the part of the player-shelf collision when the player has the correct book. It passes
    the number of books dropped off and removes them from the player list.
    '''
    def book_dropoff_col(self, player: Player, bookshelf: pygame.Rect, hud: HUD, tag: str) -> int:
        dropped = 0
        if not player.rect.colliderect(bookshelf):
            return dropped
        else:
            for book in list(player.bookscarried):
                if book.tag == tag:
                    dropped += 1
                    self.sfx_bookDrop.play()
                    player.bookscarried.remove(book)
                    hud.threebooks.remove(book)
            return dropped

    def player_pedestrian_col(self, player: Player, ped) -> bool:
        if not player.rect.colliderect(ped.rect):
            return False

        # Push player out using same logic as shelf collision
        dx_left = player.rect.right - ped.rect.left
        dx_right = ped.rect.right - player.rect.left
        dy_top = player.rect.bottom - ped.rect.top
        dy_bottom = ped.rect.bottom - player.rect.top

        min_overlap = min(dx_left, dx_right, dy_top, dy_bottom)

        if min_overlap == dx_left:
            player.rect.right = ped.rect.left
            player.velocity.x = 0
        elif min_overlap == dx_right:
            player.rect.left = ped.rect.right
            player.velocity.x = 0
        elif min_overlap == dy_top:
            player.rect.bottom = ped.rect.top
            player.velocity.y = 0
        elif min_overlap == dy_bottom:
            player.rect.top = ped.rect.bottom
            player.velocity.y = 0

        player.pos.update(player.rect.center)
        return True  # tells game.py a collision happened so it can handle the timer + cooldown

    def book_bs_col(self, book: Book, bookshelves: Bookshelves) -> bool: # consolidates shelf collisions
        return (
            book.rect.colliderect(bookshelves.bkshlf1) or
            book.rect.colliderect(bookshelves.bkshlf2) or
            book.rect.colliderect(bookshelves.bkshlf3) or
            book.rect.colliderect(bookshelves.bkshlf4) or
            book.rect.colliderect(bookshelves.bkshlf5) or
            book.rect.colliderect(bookshelves.bkshlf6) or
            book.rect.colliderect(bookshelves.bkshlf7) or
            book.rect.colliderect(bookshelves.bkshlf8) or
            book.rect.colliderect(bookshelves.bkshlf9) or
            book.rect.colliderect(bookshelves.bkshlf10) or
            book.rect.colliderect(bookshelves.bkshlf11) or
            book.rect.colliderect(bookshelves.bkshlf12)
        )

    def hud_collision(self, player: Player, hud: HUD) -> None:
        if not player.rect.colliderect(hud.rect):
            return

        player.rect.top = hud.rect.bottom
        player.velocity.y = 0
        player.pos.update(player.rect.center)

    def player_book_col(self, player: Player, book: Book, hud: HUD) -> None: # tracks whether the player is in contact with a book
        if not player.rect.colliderect(book.rect):
            return
        if len(player.bookscarried) >= 3: # player cannot have more than three books. will change to a variable amount later
            return
        else:
            player.bookscarried.append(book) # adds book to player's "inventory"
            hud.threebooks.append(book)
            self.sfx_bookPickup.play()
            book.kill() # despawns book from game


    # I changed the type hinting to int for the purposes of adding to the "carrying" value in game
    def update(self, player: Player, bookshelves: Bookshelves, books: pygame.sprite.Group, hud: HUD) -> int:
        score_add = 0
        self.player_shelf_col(player, bookshelves.bkshlf1)
        self.player_shelf_col(player, bookshelves.bkshlf2)
        self.player_shelf_col(player, bookshelves.bkshlf3)
        self.player_shelf_col(player, bookshelves.bkshlf4)
        self.player_shelf_col(player, bookshelves.bkshlf5)
        self.player_shelf_col(player, bookshelves.bkshlf6)
        self.player_shelf_col(player, bookshelves.bkshlf7)
        self.player_shelf_col(player, bookshelves.bkshlf8)
        self.player_shelf_col(player, bookshelves.bkshlf9)
        self.player_shelf_col(player, bookshelves.bkshlf10)
        self.player_shelf_col(player, bookshelves.bkshlf11)
        self.player_shelf_col(player, bookshelves.bkshlf12)

        self.hud_collision(player, hud)

        for tag, shelf in bookshelves.color_tag.items():
            score_add += self.book_dropoff_col(player, shelf, hud, tag)

        for book in list(books):
            self.player_book_col(player, book, hud)

        return score_add