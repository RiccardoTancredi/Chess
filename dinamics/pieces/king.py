from dinamics.piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        return [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def edit_moves(self, board, position, moves):
        # castling logic
        if not self.moves_history:
            row, col = position  # king position
            if not board.get_piece((row, col + 1)) and not board.get_piece((row, col + 2)):

                piece3 = board.get_piece((row, col + 3))
                if piece3 and not piece3.moves_history:
                    moves.append((row, col + 2))

            if not board.get_piece((row, col - 1)) and not board.get_piece((row, col - 2)) and not board.get_piece((row, col - 3)):

                piece4 = board.get_piece((row, col - 4))
                if piece4 and not piece4.moves_history:
                    moves.append((row, col - 2))

        return moves
