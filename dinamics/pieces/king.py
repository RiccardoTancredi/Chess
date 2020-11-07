from dinamics.piece import Piece
from dinamics.pieces.rook import Rook


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        return [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # (0,0) è corretto?

    def edit_moves(self, board, position, moves):
        # castling logic
        first_move = len(self.moves_history) == 0
        if first_move and Rook.first_rook_move:  # todo <- this is problematic
            row, col = position  # king position
            if not board.get_piece((row, col + 1)) and not board.get_piece((row, col + 2)):
                moves.append((row, col + 2))
            if not board.get_piece((row, col - 1)) and not board.get_piece((row, col - 2)) and not board.get_piece(
                    (row, col - 3)):
                moves.append((row, col - 2))

        return moves
