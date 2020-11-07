from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        return [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]

    def edit_moves(self, board, position, moves):
        for (i, j), piece in board.get_pieces(valid=True):
            if (i, j) in moves:
                if j < position[1] and i > position[0]:
                    for l in range(i, ROWS):
                        for k in range(j):
                            if (l, k) in moves:
                                moves.remove((l, k))
                elif j > position[1] and i < position[0]:
                    for l in range(i):
                        for k in range(j, COLS):
                            if (l, k) in moves:
                                moves.remove((l, k))
                elif j < position[1] and i < position[0]:
                    for l in range(i):
                        for k in range(j):
                            if (l, k) in moves:
                                moves.remove((l, k))
                elif j > position[1] and i > position[0]:
                    for l in range(i + 1, ROWS):
                        for k in range(j + 1, COLS):
                            if (l, k) in moves:
                                moves.remove((l, k))

        return moves

