from dinamics.piece import Piece
from .constants import ROWS, COLS, WHITE, BLACK
from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.bishop import Bishop
from .pieces.knight import Knight
from .pieces.rook import Rook


class Board:
    # SHORTCUTS = {"B": Bishop, "N": Knight, "Q": Queen, "R": Rook, "K": King, "P": Pawn}

    def __init__(self):
        self.board = []
        self._board_copy = []
        self.initialize()

    def initialize(self):
        for x in range(ROWS):
            self.board.append([None] * COLS)

    def get_piece(self, position) -> Piece:
        row, col = position
        if 0 <= row <= ROWS - 1 and 0 <= col <= COLS - 1:
            return self.board[row][col]
        else:
            pass

    def get_pieces(self, valid=False):
        pieces = []
        for i in range(ROWS):
            for j in range(COLS):
                piece = self.get_piece((i, j))
                if not piece and valid:
                    continue

                value = ((i, j), piece)
                pieces.append(value)
        return pieces

    def move(self, start_pos, end_pos):
        srow, scol = start_pos
        erow, ecol = end_pos
        self.board[erow][ecol] = self.board[srow][scol]
        self.board[srow][scol] = None

    def save_board(self):
        self._board_copy = []
        for i in range(ROWS):
            self._board_copy.append([])
            for j in range(COLS):
                self._board_copy[i].append(self.get_piece((i, j)))

    def rollback_board(self):
        self.board = []
        for i in range(ROWS):
            self.board.append([])
            for j in range(COLS):
                self.board[i].append(self._board_copy[i][j])

    def put(self, position, piece=None, clss=None, color=None):
        # adesso possiamo anche passargli semplicemente la classe ed il colore invece che tutto il pezzo
        row, col = position
        if clss and color:
            piece = clss(color)

        self.board[row][col] = piece

    def clear(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.board[i][j] = None

    def __repr__(self) -> str:
        emojis_w = {King: "♔", Queen: "♕", Rook: "♖", Bishop: "♗", Knight: "♘", Pawn: "♙"}
        emojis_b = {King: "♚", Queen: "♛", Rook: "♜", Bishop: "♝", Knight: "♞", Pawn: "♟"}

        text = ""
        for i in range(ROWS):
            for j in range(COLS):
                piece = self.get_piece((i, j))

                if not piece:
                    text += "󠀠⨉"
                else:
                    text += ""
                    if piece.color == WHITE:
                        text += emojis_w[piece.__class__]
                    else:
                        text += emojis_b[piece.__class__]

            text += "\n"
        text = "\n" + text
        return text


class ChessBoard(Board):
    def initialize(self):
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
            self.board.append([None] * ROWS)

        self.board.append(row2_w)
        self.board.append(row1_w)
