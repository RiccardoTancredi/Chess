from .bishop import Bishop
from .knight import Knight


class Dragon(Knight, Bishop):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        knight_moves = Knight.get_movements(self)
        bishop_moves = Bishop.get_movements(self)
        dragon_moves = list(set(knight_moves).union(set(bishop_moves)))  # remove duplicate
        return dragon_moves

    def edit_moves(self, board, position, moves):
        knight_moves = Knight.edit_moves(self, board, position, moves)
        bishop_moves = Bishop.edit_moves(self, board, position, moves)
        dragon_moves = list(set(knight_moves).union(set(bishop_moves)))  # remove duplicate
        return dragon_moves
