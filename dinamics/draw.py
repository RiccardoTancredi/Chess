import pygame

from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS, HEIGHT, WIDTH
from .board import Board
from .piece import Piece
from .pieces.queen import Queen
from .pieces.rook import Rook

C_BLACK = (0, 0, 0)
C_WHITE = (0, 0, 0)


class Draw:
    def __init__(self, win, game, assets_dir):
        self.win = win
        self.game = game
        self.scale_factor = (int(WIDTH * 50 / 400), int(HEIGHT * 50 / 400))

        self.white_pieces = {
            Pawn: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_pawn.png'), self.scale_factor),
            Knight: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_knight.png'), self.scale_factor),
            King: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_king.png'), self.scale_factor),
            Queen: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_queen.png'), self.scale_factor),
            Rook: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_rook.png'), self.scale_factor),
            Bishop: pygame.transform.scale(pygame.image.load(f'{assets_dir}/white_bishop.png'), self.scale_factor)
        }
        self.black_pieces = {
            Pawn: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_pawn.png'), self.scale_factor),
            Knight: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_knight.png'), self.scale_factor),
            King: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_king.png'), self.scale_factor),
            Queen: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_queen.png'), self.scale_factor),
            Rook: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_rook.png'), self.scale_factor),
            Bishop: pygame.transform.scale(pygame.image.load(f'{assets_dir}/black_bishop.png'), self.scale_factor)
        }

    def draw_squares(self):
        self.win.fill(C_BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.win, C_WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.game.board.get_piece((row, col))
                if piece:
                    image = None
                    if piece.color == WHITE:
                        image = self.white_pieces[piece.__class__]
                    elif piece.color == BLACK:
                        image = self.black_pieces[piece.__class__]

                    self.win.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
                else:
                    pass
                # here we have to add the initial configuration of the chess board
                # so we have to define first the piece class and all the pieces classes:
                # pieces = King, Queen, Rook, Bishop, Knight, Pawn

    def update(self):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.draw_squares()
        self.draw_pieces()
