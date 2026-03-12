import pygame

from .player import Player
from .bookshelves import Bookshelves
from .books import Book
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

    def player_book_col(self, player: Player, book: Book) -> int: # tracks whether the player is in contact with a book
        if not player.rect.colliderect(book.rect):
            return 0
        else:
            book.kill()
            return 1


    # I changed the type hinting to int for the purposes of adding to the "carrying" value in game
    def update(self, player: Player, bookshelves: Bookshelves, books: pygame.sprite.Group) -> int:
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

        for book in list(books):
            score_add += self.player_book_col(player, book)
        return score_add