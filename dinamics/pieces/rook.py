from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True

    def get_available_moves(self, position):
        pass

    def first_rook_move(self):
        if self.first_move:
            self.first_move = False

    def get_movements_test(self):
        basic_moves = []
        for j in range(-COLS + 1, COLS):
            basic_moves.append((0, j))
        for i in range(-ROWS + 1, ROWS):
            basic_moves.append((i, 0))
        return basic_moves

    def delete_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                if_black_piece = 0
                piece = board.get_piece((i, j))
                if piece and (i, j) in moves:
                    if self.color != piece.color and self.color == "BLACK":
                        if_black_piece = -1
                    # if self.color == piece.color:
                    if i == position[0]:
                        if j > position[1]:
                            for l in range(j - if_black_piece, COLS + 1):
                                if (i, l) in moves:
                                    moves.remove((i, l))
                        elif j < position[1]:
                            for l in range(0, j - if_black_piece):
                                if (i, l) in moves:
                                    moves.remove((i, l))
                    elif j == position[1]:
                        if i > position[0]:
                            for k in range(i - if_black_piece, ROWS + 1):
                                if (k, j) in moves:
                                    moves.remove((k, j))
                        elif i < position[0]:
                            for k in range(0, i - if_black_piece):
                                if (k, j) in moves:
                                    moves.remove((k, j))

        return moves

    def eat_piece(self, board, position, moves):
        return moves
