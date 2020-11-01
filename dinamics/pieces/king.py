from dinamics.piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_available_moves(self, position):
        pass

    def get_movements_test(self):
        return [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    def delete_moves(self, board, position, moves):
        return moves

    def eat_piece(self, board, position, moves):
        return moves

    def castling(self):
        pass

