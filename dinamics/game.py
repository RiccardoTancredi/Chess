from dinamics.board import Board
from dinamics.constants import WHITE, BLACK
from dinamics.constants import ROWS, COLS


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move_piece(self, piece_pos, position, color):
        piece = self.board.get_piece(piece_pos)
        moves = piece.get_available_moves(piece_pos, color)

        # it's just a basic move, need improvements
        if position in moves:
            self.board.move(piece_pos, position)
        

    def move_piece_test(self, start, end, check=True):
        piece = self.board.get_piece(start)
        if not piece:
            return

        if check:  # se vogliamo controllare che sia una mossa valida. potremo non volerlo quando usiamo la grafica
            moves = piece.get_movements_test()
            if end not in moves:
                return

        self.board.move(start, end)
        piece.on_move(start, end)  # chiamiamo questo metodo una volta che modifichiamo un pezzo
        self.change_turn()

    def get_possible_moves(self, position):
        piece = self.board.get_piece(position)
        if not piece:
            return []

        moves = piece.get_movements_test()
        moves = self._add_moves_to_pos(piece, position, moves)
        moves = self._trim_moves(moves)
        moves = self._delete_moves(piece, self.board, position, moves)
        moves = self._eat_piece(piece, self.board, position, moves)
        # vogliamo iterare le mosse e allo stesso tempo modificare la lista, quindi dobbiamo crearne un'altra con list(...)
        for move in list(moves):
            other = self.board.get_piece(move)
            if not other:
                continue

            if other.color == piece.color:
                moves.remove(move)
        return moves

    def _add_moves_to_pos(self, piece, position, moves):

        # translate moves coordinate (x, y) to board coordinate (row, col)
        # if it's white we have to reverse the row because the y axes goes down

        moves_translated = []
        for move in moves:
            move_t = (move[1], move[0])
            if piece.color == WHITE:
                move_t = (-move[1], move[0])
            moves_translated.append(move_t)
        moves = moves_translated

        affine_moves = []
        for move in moves:  # translate the moves from (0,0) to position
            aff_move = (move[0] + position[0], move[1] + position[1])
            affine_moves.append(aff_move)

        return affine_moves

    # elimina le mosse che sono al di fuori della board
    def _trim_moves(self, moves):
        trimmed = []
        for move in moves:
            if (0 <= move[0] < COLS) and (0 <= move[1] < ROWS):
                trimmed.append(move)

        return trimmed

    def _delete_moves(self, piece, board, position, moves):
        return piece.delete_moves(board, position, moves)

    def _eat_piece(self, piece, board, position, moves):
        return piece.eat_piece(board, position, moves) 

    def change_turn(self):
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else:
            self.turn = "WHITE"
        # return turn