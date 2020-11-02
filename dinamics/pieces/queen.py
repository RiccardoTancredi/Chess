from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS

from .bishop import Bishop
from .rook import Rook


class Queen(Rook, Bishop):
    def __init__(self, color):
        super().__init__(color)

    def get_available_moves(self, position):
        pass

    def get_movements_test(self):
        rook_basic_moves = super(Rook, self).get_movements_test()
        bishop_basic_moves = super(Bishop, self).get_movements_test()
        queen_basic_moves = bishop_basic_moves + rook_basic_moves
        return queen_basic_moves

    def delete_moves(self, board, position, moves):
        rook_moves = Rook.delete_moves(self, board, position, moves)
        bishop_moves = Bishop.delete_moves(self, board, position, moves)
        queen_moves = rook_moves + bishop_moves
        return queen_moves

    def eat_piece(self, board, position, moves):
        return moves
