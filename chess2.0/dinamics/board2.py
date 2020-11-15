from dinamics.piece import Piece
from .constants2 import ROWS, COLS, WHITE, BLACK
from .pieces.pawn import Pawn
from .pieces.king import King
from .pieces.queen import Queen
from .pieces.bishop import Bishop
from .pieces.knight import Knight
from .pieces.rook import Rook
from .pieces.dragon import Dragon

class Board:
    # SHORTCUTS = {"B": Bishop, "N": Knight, "Q": Queen, "R": Rook, "K": King, "P": Pawn}

    def __init__(self):
        self.board = []
        self._board_copy = []
        self._create_board()

    def _create_board(self):
        row1_w = [Rook(WHITE), Knight(WHITE), Dragon(WHITE), Bishop(WHITE), Queen(WHITE),
                  King(WHITE), Bishop(WHITE), Dragon(WHITE), Knight(WHITE), Rook(WHITE)]
        row2_w = []
        for i in range(ROWS):
            row2_w.append(Pawn(WHITE))

        row1_b = [Rook(BLACK), Knight(BLACK), Dragon(BLACK), Bishop(BLACK), Queen(BLACK),
                  King(BLACK), Bishop(BLACK), Dragon(BLACK), Knight(BLACK), Rook(BLACK)]
        row2_b = []
        for i in range(ROWS):
            row2_b.append(Pawn(BLACK))

        self.board.append(row1_b)
        self.board.append(row2_b)

        for x in range(6):
            self.board.append([None] * ROWS)

        self.board.append(row2_w)
        self.board.append(row1_w)

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

    def move(self, start_pos, end_pos, piece):
        srow, scol = start_pos
        erow, ecol = end_pos
        if isinstance(piece, King) and abs(ecol - scol) == 3:
            if ecol - scol > 0:  # the king is doing the short castling
                self.board[srow][scol + 1] = self.board[srow][ROWS - 1]
                self.board[srow][ROWS - 1] = None
            if ecol - scol < 0:  # long castling
                self.board[srow][scol - 1] = self.board[srow][0]
                self.board[srow][0] = None

        elif isinstance(piece, Pawn):
            # this means that the pawn is moving diagonally
            if not self.get_piece(end_pos) and abs(ecol - scol) == 1:
                # if ecol - scol > 0:  # pawn en passant to the right
                # self.board[erow][ecol], self.board[srow][scol] = self.board[srow][scol], None
                self.board[srow][ecol] = None
                # if ecol - scol < 0:  # pawn en passant to the left
                #     self.board[erow][ecol], self.board[srow][scol-1] = self.board[srow][scol], None

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

    # def _create_from_string(self, board_string: str):
    #     rows = []
    #     max_w = 0
    #     board_string = board_string.strip()
    #     for line in board_string.split("\n"):
    #         line = line.strip()
    #         if not line:
    #             continue
    #
    #         pieces_raw = line.split(" ")
    #         pieces = []
    #         for piece_raw in pieces_raw:
    #             piece_raw = piece_raw.strip()
    #
    #             if not piece_raw:
    #                 continue
    #
    #             if piece_raw[0] == "-":
    #                 pieces.append(None)
    #                 continue
    #
    #             clss = Board.SHORTCUTS.get(piece_raw[0])
    #             if not clss or not len(piece_raw) == 2:
    #                 continue
    #
    #             color = WHITE
    #             if piece_raw[1] == "b":
    #                 color = BLACK
    #
    #             pieces.append(clss(color))
    #
    #         if len(pieces) > max_w:
    #             max_w = len(pieces)
    #
    #         rows.append(pieces)
    #
    #     # crea una scacchiera vuota
    #     for _ in range(ROWS):
    #         self.board.append([None] * COLS)
    #
    #     start_w = (COLS - max_w) // 2
    #     start_h = (ROWS - len(rows) - 1) // 2
    #
    #     for j in range(start_h, start_h + len(rows)):
    #         row = rows[j - start_h]
    #         k = start_w + len(row)
    #         self.board[j][start_w: k] = row

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
