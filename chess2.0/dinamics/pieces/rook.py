from dinamics.piece import Piece
from dinamics.constants2 import ROWS, COLS


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def get_movements(self):
        basic_moves = []
        for j in range(-COLS + 1, COLS):
            basic_moves.append((0, j))
        for i in range(-ROWS + 1, ROWS):
            basic_moves.append((i, 0))
        return basic_moves

    def edit_moves(self, board, position, moves):
        for (i, j), piece in board.get_pieces(valid=True):
            if (i, j) in moves:
                if i == position[0]:
                    if j > position[1]:
                        for l in range(j + 1, COLS + 1):
                            if (i, l) in moves:
                                moves.remove((i, l))
                    elif j < position[1]:
                        for l in range(0, j):
                            if (i, l) in moves:
                                moves.remove((i, l))
                elif j == position[1]:
                    if i > position[0]:
                        for k in range(i + 1, ROWS + 1):
                            if (k, j) in moves:
                                moves.remove((k, j))
                    elif i < position[0]:
                        for k in range(0, i):
                            if (k, j) in moves:
                                moves.remove((k, j))

        return moves