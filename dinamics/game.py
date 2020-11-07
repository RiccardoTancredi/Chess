from dinamics.board import Board
from dinamics.constants import WHITE, BLACK
from dinamics.constants import ROWS, COLS
from dinamics.pieces.king import King
from dinamics.pieces.pawn import Pawn


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = WHITE
        self.notation = []

    def move_piece(self, start, end, check=True):
        piece = self.board.get_piece(start)
        if not piece:
            return

        if check:  # se vogliamo controllare che sia una mossa valida. potremo non volerlo quando usiamo la grafica
            moves = piece.get_movements()  # todo
            if end not in moves:
                return

        self.board.move(start, end, piece)
        piece.on_move(start, end)  # chiamiamo questo metodo una volta che modifichiamo un pezzo
        self.update_notation(piece, start, end)
        if isinstance(piece, Pawn) and (end[0] == 0 or end[0] == ROWS - 1):
            piece = self._promotion(piece, self.board)
        self.change_turn()

    def get_possible_moves(self, position):
        piece = self.board.get_piece(position)
        if not piece:
            return []

        moves = piece.get_movements()
        moves = self._add_moves_to_pos(piece, position, moves)
        moves = self._remove_outside_board(moves)
        moves = self._delete_moves(piece, self.board, position, moves)
        moves = self._add_moves(piece, self.board, position, moves)

        moves = self._remove_fixed_moves(position, piece, moves)

        # todo fare un metodo edit_moves e mettere lì tutta la logica della modifica delle mosse (che sostituirà castling/en_passant/delete_moves/add_moves
        if isinstance(piece, King):
            moves = self._castling(piece, self.board, position, moves)
        if isinstance(piece, Pawn):
            moves = self._en_passant(piece, self.board, position, moves, self.notation)
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
    def _remove_outside_board(self, moves):
        trimmed = []
        for move in moves:
            if (0 <= move[0] < COLS) and (0 <= move[1] < ROWS):
                trimmed.append(move)

        return trimmed

    def _remove_fixed_moves(self, position, piece, moves):
        king_pos = None
        # cerchiamo il re
        for (j, k), opiece in self.board.get_pieces(valid=True):
            if opiece.color != piece.color:
                continue
            if isinstance(opiece, King):
                king_pos = (j, k)
                break

        # per ogni mossa del pezzo che voglio muovere
        for move in list(moves):
            self.board.save_board()  # salviamo la board come è
            self.board.move(position, move, piece)  # moviamo il pezzo secondo una delle mosse possibili
            for (j, k), opiece in self.board.get_pieces(valid=True):  # per ogni pezzo della board
                if opiece.color == piece.color:
                    continue
                # per ogni casella nemica
                # adesso calcoliamo tutti i movimenti che quella pedina nemica può fare supponendo che io abbia fatto quella mossa
                omoves = opiece.get_movements()
                omoves = self._add_moves_to_pos(opiece, (j, k), omoves)
                omoves = self._remove_outside_board(omoves)
                omoves = self._delete_moves(opiece, self.board, (j, k), omoves)
                omoves = self._add_moves(opiece, self.board, (j, k), omoves)

                # se fra le mosse che può fare c'è quella di catturare il re, allora la mossa non si può fare
                if king_pos in omoves:
                    moves.remove(move)
                    break
            self.board.rollback_board()  # rimettiamo la board com'era prima della mossa
        return moves

    def _delete_moves(self, piece, board, position, moves):
        return piece.delete_moves(board, position, moves)

    def _add_moves(self, piece, board, position, moves):
        return piece.add_moves(board, position, moves)

    def _castling(self, king, board, position, moves):
        return king.castling(board, position, moves)

    def _en_passant(self, pawn, board, position, moves, notation):
        return pawn.en_passant(board, position, moves, notation)

    def _promotion(self, pawn, board):
        return pawn.promotion(board)

    def change_turn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE

    def update_notation(self, piece, start, end):
        self.notation.append([piece.color, piece.__class__.__name__, start, end])
