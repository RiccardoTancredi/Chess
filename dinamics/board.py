from dinamics.piece import Piece
from .constants import ROWS, COLS, WHITE, BLACK
from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.bishop import Bishop
from .pieces.knight import Knight
from .pieces.rook import Rook


class Board:
    def __init__(self):
        self.board = []

        self._create_board()

    def _create_board(self):
        row1_w = [Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
                  King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)]
        row2_w = []
        for i in range(ROWS):
            row2_w.append(Pawn(WHITE))

        row1_b = [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
                  King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)]
        row2_b = []
        for i in range(ROWS):
            row2_b.append(Pawn(BLACK))

        self.board.append(row1_b)
        self.board.append(row2_b)

        for x in range(4):
            self.board.append([None] * ROWS)  # A list of 8 empty elements

        self.board.append(row2_w)
        self.board.append(row1_w)

    def get_piece(self, position) -> Piece:
        row, col = position
        if 0 <= row <= ROWS - 1 and 0 <= col <= COLS - 1:
            return self.board[row][col]
        else:
            pass

    def move(self, start_pos, end_pos, piece):
        srow, scol = start_pos
        erow, ecol = end_pos
        if piece.__class__.__name__ == "King" and abs(ecol - scol) == 2:
            if ecol - scol > 0:  # the king is doing the short castling
                self.board[srow][scol + 1], self.board[srow][ROWS - 1] = self.board[srow][ROWS - 1], None
            if ecol - scol < 0:  # long castling
                self.board[srow][scol - 1], self.board[srow][0] = self.board[srow][0], None
        if piece.__class__.__name__ == "Pawn":
            if self.get_piece(end_pos) == None and abs(ecol - scol) == 1: # this means that the pawn is moving diagonally
                # if ecol - scol > 0:  # pawn en passant to the right
                # self.board[erow][ecol], self.board[srow][scol] = self.board[srow][scol], None
                self.board[srow][ecol] = None
                # if ecol - scol < 0:  # pawn en passant to the left
                #     self.board[erow][ecol], self.board[srow][scol-1] = self.board[srow][scol], None
        
        self.board[erow][ecol] = self.board[srow][scol]
        self.board[srow][scol] = None

        
