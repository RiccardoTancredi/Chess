import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLACK, GREY, BLACK_PIECES, WHITE_PIECES, BLACK_PAWN, WHITE_PAWN
from .piece import Piece
from .Pieces.Pawn import Pawn
from .Pieces.King import King
from .Pieces.Queen import Queen 
from .Pieces.Bishop import Bishop
from .Pieces.Knight import Knight
from .Pieces.Rook import Rook 

class Board:
    def __init__(self, win):
        self.board = []
        self.win = win
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row == 0:
                    self.board[row].append(BLACK_PIECES[col])
                elif row == ROWS - 1:
                    self.board[row].append(WHITE_PIECES[col])
                elif row == 1:
                    self.board[row].append(Piece(row, col, BLACK, "Pawn", self.win).select_piece()) # like this all the others
                    # self.board[row].append(Pawn(BLACK).select)
                elif row == ROWS - 2:
                    self.board[row].append(WHITE_PAWN)
                else:
                    self.board[row].append(0)
                # here we have to add the initial configuration of the chess board
                # so we have to define first the piece class and all the pieces classes:
                # Pieces = King, Queen, Rook, Bishop, Knight, Pawn
    
    def get_piece(self, row, col):
        return self.board[row][col]

