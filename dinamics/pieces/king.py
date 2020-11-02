from dinamics.piece import Piece
from .rook import Rook

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True

    def get_available_moves(self, position):
        pass

    def on_move(self, start, end):
        if self.first_move:
            self.first_move = False

    def get_movements_test(self):
        return [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    def delete_moves(self, board, position, moves):
        return moves

    def eat_piece(self, board, position, moves):
        return moves

    def first_king_move(self):
        if self.first_move:
            self.first_move = False

    def castling(self, board, position,moves):
        if self.first_move and Rook.first_rook_move:
            row, col = position #king position 
            if not board.get_piece((row, col + 1)) and not board.get_piece((row, col + 2)):
                moves.append((row, col+2))
            if not board.get_piece((row, col - 1)) and not board.get_piece((row, col - 2)) and not board.get_piece((row, col - 3)):
                moves.append((row, col-2))
        return moves

