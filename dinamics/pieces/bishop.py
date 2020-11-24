from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):

        count = min(ROWS, COLS)
        moves = set()
        for k in range(-count, count):
            moves.add((k, k))
            moves.add((k, -k))
        moves.remove((0, 0))
        return list(moves)

        # return [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
        #         (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
        #         (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
        #         (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]

    def edit_moves(self, board, position, moves):

        row, col = position
        # tutte le mosse possibili mosse (anche non legali) verso NE, NW, SE e SW
        moves_ne = [(row - k, col + k) for k in range(1, min(row + 1, COLS - col))]
        moves_nw = [(row - k, col - k) for k in range(1, min(row + 1, col + 1))]
        moves_se = [(row + k, col + k) for k in range(1, min(ROWS - row, COLS - col))]
        moves_sw = [(row + k, col - k) for k in range(1, min(ROWS - row, col + 1))]

        good_moves = set()
        # qui filtriamo le mosse tenendo soltanto quelle legali per ogni direzione
        good_moves = good_moves.union(self._keep_until_piece(board, moves_ne, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_nw, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_se, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_sw, moves))

        # moves = bishop_moves
        # for (i, j), piece in board.get_pieces(valid=True):
        #     if (i, j) in moves:
        #         if j < position[1] and i > position[0]:
        #             for l in range(i, ROWS):
        #                 for k in range(j):
        #                     if (l, k) in moves:
        #                         moves.remove((l, k))
        #         elif j > position[1] and i < position[0]:
        #             for l in range(i):
        #                 for k in range(j, COLS):
        #                     if (l, k) in moves:
        #                         moves.remove((l, k))
        #         elif j < position[1] and i < position[0]:
        #             for l in range(i):
        #                 for k in range(j):
        #                     if (l, k) in moves:
        #                         moves.remove((l, k))
        #         elif j > position[1] and i > position[0]:
        #             for l in range(i + 1, ROWS):
        #                 for k in range(j + 1, COLS):
        #                     if (l, k) in moves:
        #                         moves.remove((l, k))

        return list(good_moves)

    # come la torre
    def _keep_until_piece(self, board, moves, legal_moves):
        good_moves = set()
        for move in moves:
            piece = board.get_piece(move)
            if piece:
                if piece.color != self.color and move in legal_moves:
                    good_moves.add(move)

                break

            if move in legal_moves:
                good_moves.add(move)
        return good_moves
