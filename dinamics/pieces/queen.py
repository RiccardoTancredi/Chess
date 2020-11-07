from .bishop import Bishop
from .rook import Rook


class Queen(Rook, Bishop):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        rook_moves = Rook.get_movements(self)
        bishop_moves = Bishop.get_movements(self)
        queen_moves = list(set(bishop_moves).union(set(rook_moves)))  # remove duplicate
        return queen_moves

    def delete_moves(self, board, position, moves):
        rook_moves = Rook.delete_moves(self, board, position, moves)
        bishop_moves = Bishop.delete_moves(self, board, position, moves)
        queen_moves = list(set(bishop_moves).union(set(rook_moves)))  # remove duplicate
        return queen_moves
