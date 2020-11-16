from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_movements(self):
        basic_moves = []
        for j in range(-COLS + 1, COLS):
            basic_moves.append((0, j))
        for i in range(-ROWS + 1, ROWS):
            basic_moves.append((i, 0))
        return basic_moves

    def edit_moves(self, board, position, moves):
        row, col = position
        # crea 4 vettori dove metti 1) le mosse a sinistra della torre 2) le mosse a destra
        # 3) le mosse sopra 4) le mosse sotto
        # la sintassi è quella delle "comprehension list"
        moves_left = [move for move in moves if move[0] == row and move[1] < col]
        moves_right = [move for move in moves if move[0] == row and move[1] > col]
        moves_up = [move for move in moves if move[1] == col and move[0] < row]
        moves_down = [move for move in moves if move[1] == col and move[0] > row]

        # ordiniamo questi 4 vettori in base alle colonne se le mosse sono orizzontali e alle righe se verticaloùi
        # key= specifica su quale attributo della tupla fare l'ordine, lambda x è una shortcut per definire
        # una funzione al volo, che in questo caso mi dice rispetto a cosa ordinare, è equivalente a
        # def func(x):
        #   return x[1]
        # sorted(moves_left, key=func, reverse=True)
        # ordiniamo in ordine decrescente quelle a sinistra e quelle sopra, in quanto voglio prima quelli più vicini
        # alla torre
        moves_left = sorted(moves_left, key=lambda x: x[1], reverse=True)
        moves_right = sorted(moves_right, key=lambda x: x[1])
        moves_up = sorted(moves_up, key=lambda x: x[0], reverse=True)
        moves_down = sorted(moves_down, key=lambda x: x[0])

        # chiamiamo il metodo _keep_until_piece per ognuno di questi 4 vettori
        good_moves = set()
        good_moves = good_moves.union(self._keep_until_piece(board, moves_left))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_right))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_up))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_down))

        return list(good_moves)

        # for (i, j), piece in board.get_pieces(valid=True):
        #     if (i, j) in moves:
        #         if i == position[0]:
        #             if j > position[1]:
        #                 for l in range(j + 1, COLS + 1):
        #                     if (i, l) in moves:
        #                         moves.remove((i, l))
        #             elif j < position[1]:
        #                 for l in range(0, j):
        #                     if (i, l) in moves:
        #                         moves.remove((i, l))
        #         elif j == position[1]:
        #             if i > position[0]:
        #                 for k in range(i + 1, ROWS + 1):
        #                     if (k, j) in moves:
        #                         moves.remove((k, j))
        #             elif i < position[0]:
        #                 for k in range(0, i):
        #                     if (k, j) in moves:
        #                         moves.remove((k, j))
        #
        # return moves

    # praticamente, dato che sono in ordine, cioè il primo è il più vicino alla torre e l'ultimo più lontano
    # (ricordando che sono mosse o sopra o a destra o a sinistra o sotto della torre) appena troviamo un pezzo,
    # tutte quelle dopo sono mosse non valide, aggiungo la mossa del pezzo se è un nemico
    def _keep_until_piece(self, board, moves):
        good_moves = set()
        for move in moves:
            piece = board.get_piece(move)
            if piece:
                if piece.color != self.color:
                    good_moves.add(move)
                break

            good_moves.add(move)
        return good_moves
