from dinamics.constants import ROWS
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

                r_rook = board.get_piece((row, col + 3))
                if r_rook and not r_rook.moves_history:
                    moves.append((row, col + 2))

            if not board.get_piece((row, col - 1)) and not board.get_piece((row, col - 2)) and not board.get_piece((row, col - 3)):

                l_rook = board.get_piece((row, col - 4))
                if l_rook and not l_rook.moves_history:
                    moves.append((row, col - 2))

        return moves

    def side_effects(self, board, start, end):
        srow, scol = start
        erow, ecol = end
        if abs(ecol - scol) == 2:
            if ecol - scol > 0:  # the king is doing the short castling
                board.move((srow, ROWS - 1), (srow, scol + 1))
                # self.board[srow][scol + 1] = self.board[srow][ROWS - 1]
                # self.board[srow][ROWS - 1] = None
            if ecol - scol < 0:  # long castling
                board.move((srow, 0), (srow, scol - 1))
                # self.board[srow][scol - 1] = self.board[srow][0]
                # self.board[srow][0] = None
