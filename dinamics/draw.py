import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, ROWS, COLS, BLACK_PIECES, WHITE_PIECES, BLACK_PAWN, WHITE_PAWN
from .board import Board
from .piece import Piece

class Draw:
    def __init__(self, win):
        self.win = win
        self.board = Board(self.win)
        
    def squares(self):
        self.win.fill(BLACK)
        self.board.create_board()
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(self.win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def draw_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.get_piece(row,col)
                if piece != 0:
                    self.win.blit(piece, (col*SQUARE_SIZE, row*SQUARE_SIZE))
                else:
                    pass
                # here we have to add the initial configuration of the chess board
                # so we have to define first the piece class and all the pieces classes:
                # Pieces = King, Queen, Rook, Bishop, Knight, Pawn
    
    def update(self):
        self.draw()
        pygame.display.update()

    def draw(self):
        self.squares()
        self.draw_pieces()