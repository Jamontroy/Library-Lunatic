import pygame

from .player import Player
from .bookshelves import Bookshelves
from .books import Book
from .hud import HUD

class Collisions: 

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
    def book_dropoff_col(self, player: Player, bookshelf: pygame.Rect, tag: str) -> int:
        dropped = 0
        if not player.rect.colliderect(bookshelf):
            return dropped
        else:
            for book in list(player.bookscarried):
                if book.tag == tag:
                    dropped += 1
                    player.bookscarried.remove(book)
            return dropped


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

    def player_book_col(self, player: Player, book: Book) -> None: # tracks whether the player is in contact with a book
        if not player.rect.colliderect(book.rect):
            return
        if len(player.bookscarried) >= 3: # player cannot have more than three books. will change to a variable amount later
            return
        else:
            player.bookscarried.append(book) # adds book to player's "inventory"
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
            score_add += self.book_dropoff_col(player, shelf, tag)

        for book in list(books):
            self.player_book_col(player, book)

        return score_add