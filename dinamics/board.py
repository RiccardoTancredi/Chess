# import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLACK
from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.bishop import Bishop
from .pieces.knight import Knight
from .pieces.rook import Rook


# class Board:
#     def __init__(self, win):
#         self.board = []
#         self.win = win
#         self.create_board()
#
#     def create_board(self):
#         for row in range(ROWS):
#             self.board.append([])
#             for col in range(COLS):
#                 if row == 0:
#                     self.board[row].append(BLACK_PIECES[col])
#                 elif row == ROWS - 1:
#                     self.board[row].append(WHITE_PIECES[col])
#                 elif row == 1:
#                     self.board[row].append(
#                         Piece(row, col, BLACK, "Pawn", self.win).select_piece())  # like this all the others
#                     # self.board[row].append(Pawn(BLACK).select)
#                 elif row == ROWS - 2:
#                     self.board[row].append(WHITE_PAWN)
#                 else:
#                     self.board[row].append(0)
#                 # here we have to add the initial configuration of the chess board
#                 # so we have to define first the piece class and all the pieces classes:
#                 # pieces = King, Queen, Rook, Bishop, Knight, Pawn
#
#     def get_piece(self, row, col):
#         return self.board[row][col]


class Board:
    def __init__(self):
        self._board = []

        self._create_board()

    def _create_board(self):
        row1_w = [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
                  King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)]
        row2_w = [Pawn(WHITE)] * 8  # A list of 8 pawns

        row1_b = [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
                  King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)]
        row2_b = [Pawn(BLACK)] * 8

        self._board.append(row1_w)
        self._board.append(row2_w)
        for x in range(4):
            self._board.append([None] * 8)  # A list of 8 empty elements

        self._board.append(row2_b)
        self._board.append(row1_b)

    def get_piece(self, position):
        row, col = position
        return self._board[row][col]

    def move(self, start_pos, end_pos):
        srow, scol = start_pos
        erow, ecol = end_pos
        self._board[erow][ecol] = self._board[srow][scol]
        self._board[srow][scol] = None
