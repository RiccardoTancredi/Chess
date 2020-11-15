from dinamics.piece import Piece
from dinamics.constants2 import ROWS, COLS


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        return [(1, 2), (2, 1), (-1, 2), (-2, 1),
                (-1, -2), (-2, -1), (1, -2), (2, -1)]

    def edit_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                piece = board.get_piece((i, j))
                if piece and piece.color == self.color and (i, j) in moves:
                    moves.remove((i, j))
        return moves
