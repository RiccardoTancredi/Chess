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
        # tutte le mosse possibili mosse (anche non legali) verso sinistra, destra, sopra e sotto
        moves_left = [(row, col - k) for k in range(1, col + 1)]
        moves_right = [(row, col + k) for k in range(1, COLS - col)]
        moves_up = [(row - k, col) for k in range(1, row + 1)]
        moves_down = [(row + k, col) for k in range(1, ROWS - row)]

        good_moves = set()
        # qui filtriamo le mosse tenendo soltanto quelle legali per ogni direzione
        good_moves = good_moves.union(self._keep_until_piece(board, moves_left, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_right, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_up, moves))
        good_moves = good_moves.union(self._keep_until_piece(board, moves_down, moves))

        return list(good_moves)

    # praticamente, dato che sono in ordine, cioè il primo è il più vicino alla torre e l'ultimo più lontano
    # (ricordando che sono mosse o sopra o a destra o a sinistra o sotto della torre) appena troviamo un pezzo,
    # tutte quelle dopo sono mosse non valide, aggiungo la mossa del pezzo se è un nemico
    def _keep_until_piece(self, board, moves, legal_moves):
        good_moves = set()
        for move in moves:
            piece = board.get_piece(move)
            if piece:
                # abbiamo trovato un pezzo, quindi se è nemico aggiungiamo la mossa, altrimenti la saltiamo
                # in ogni caso fermiamo il ciclo in quanto nessun'altra mossa dopo potrà essere legale
                if piece.color != self.color and move in legal_moves:
                    good_moves.add(move)
                break

            if move in legal_moves:
                good_moves.add(move)
        return good_moves
