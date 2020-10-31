from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_available_moves(self, position):
        pass

    def get_movements_test(self):
        return [(1, 2), (2, 1), (-1, 2), (-2, 1),       # le 4 possibili L (se sono in (0,0))
                (-1, -2), (-2, -1), (1, -2), (2, -1)]

    def delete_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                piece = board.get_piece((i, j))
                if piece and piece.color == self.color and (i, j) in moves:
                    moves.remove((i, j))
        return moves

    def eat_piece(self, board, position, moves):
        return moves
