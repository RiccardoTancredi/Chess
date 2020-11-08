from dinamics.piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        return [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # (0,0) è corretto?

    def edit_moves(self, board, position, moves):
        # castling logic
        if not self.moves_history:  # todo <- this is problematic
            row, col = position  # king position
            if not board.get_piece((row, col + 1)) and not board.get_piece((row, col + 2)) and board.get_piece((row, col + 3)) and not board.get_piece((row, col + 3)).moves_history:
                moves.append((row, col + 2))
            if not board.get_piece((row, col - 1)) and not board.get_piece((row, col - 2)) and not board.get_piece((row, col - 3)) and board.get_piece((row, col - 4)) and not board.get_piece((row, col - 4)).moves_history:
                moves.append((row, col - 2))

        return moves
