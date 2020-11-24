from dinamics.board import Board, ChessBoard
from dinamics.constants import WHITE, BLACK
from dinamics.constants import ROWS, COLS
from dinamics.pieces.king import King
from dinamics.pieces.pawn import Pawn


class Game:
    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = ChessBoard()

        self.turn = WHITE
        self.notation = []
        self.need_promotion = None
        self._player_moves = {}

        self.initialize()

    def initialize(self):
        self._player_moves[WHITE] = self._get_all_player_moves(WHITE)
        self._player_moves[BLACK] = self._get_all_player_moves(BLACK)

    def get_possible_moves(self, position):
        piece = self.board.get_piece(position)
        if not piece:
            return []

        moves = self._get_correct_moves(piece, position)
        moves = self._remove_pinned_moves(position, piece, moves)

        return moves

    def move_piece(self, start, end, check=False):
        if self.need_promotion:  # se c'è un pezzo da promuovere promuovilo prima di procedere
            return

        piece = self.board.get_piece(start)
        if not piece:
            return

        if check:  # se vogliamo controllare che sia una mossa valida. potremo non volerlo quando usiamo la grafica
            pass  # todo

        piece.side_effects(self.board, start, end)
        self.board.move(start, end)
        piece.after_move(start, end)

        self.update_notation(piece, start, end)

        if isinstance(piece, Pawn) and self._is_at_the_end(end, piece):
            self.need_promotion = end

        if not self.need_promotion:  # Se c'è un pezzo da promuovere non cambiare il turno
            self.end_turn()

    def end_turn(self):
        self._player_moves[self.turn] = self._get_all_player_moves(self.turn)
        self.change_turn()

    def _get_correct_moves(self, piece, position):
        moves = piece.get_movements()
        moves = self._add_moves_to_pos(piece, position, moves)
        moves = self._remove_outside_board(moves)
        # moves = self._remove_allies_moves(piece, moves)
        moves = piece.edit_moves(self.board, position, moves)

        if isinstance(piece, Pawn):
            moves = piece.en_passant(self.board, position, moves, self.notation)

        moves = self._remove_allies_moves(piece, moves)
        return moves

    def _add_moves_to_pos(self, piece, position, moves):
        # translate moves coordinate (x, y) to board coordinate (row, col)
        # if it's white we have to reverse the row because the y axes goes down
        moves_translated = []
        for move in moves:
            if piece.color == WHITE:
                move_t = (-move[1], move[0])
            else:
                move_t = (move[1], move[0])

            moves_translated.append(move_t)

        moves = moves_translated

        affine_moves = []
        for move in moves:  # translate the moves from (0,0) to position
            aff_move = (move[0] + position[0], move[1] + position[1])
            affine_moves.append(aff_move)

        return affine_moves

    def _remove_outside_board(self, moves):
        trimmed = []
        for move in moves:
            if (0 <= move[0] < COLS) and (0 <= move[1] < ROWS):
                trimmed.append(move)

        return trimmed

    def _remove_allies_moves(self, piece, moves):
        for move in list(moves):
            other = self.board.get_piece(move)
            if not other:
                continue

            if other.color == piece.color:
                moves.remove(move)
        return moves

    def _remove_pinned_moves(self, position, piece, moves):
        # se la pedina cliccata è il re
        if isinstance(piece, King):
            opposite = self._get_other_player(piece.color)
            enemy_moves = self._player_moves[opposite]
            for move in list(moves):
                if move in enemy_moves:
                    moves.remove(move)

            for (j, k) in list(moves):
                if k - position[1] == -2:
                    if (j, k + 1) not in moves or (j, k - 1) in enemy_moves:
                        moves.remove((j, k))

                elif k - position[1] == 2:
                    if (j, k - 1) not in moves or (j, k + 1) in enemy_moves:
                        moves.remove((j, k))

            return moves

        # cerchiamo il re
        king_pos = None
        for (j, k), opiece in self.board.get_pieces(valid=True):
            if opiece.color != piece.color:
                continue
            if isinstance(opiece, King):
                king_pos = (j, k)
                break

        if not king_pos:  # per i test
            return moves

        # per ogni mossa del pezzo che voglio muovere
        for move in list(moves):
            self.board.save_board()  # salviamo la board come è
            # moviamo il pezzo secondo una delle mosse possibili
            # nel move c'è della logica che potrebbe dar problemi
            self.board.move(position, move)
            for (j, k), opiece in self.board.get_pieces(valid=True):  # per ogni pezzo della board
                # se è un alleato saltiamo
                if opiece.color == piece.color:
                    continue

                # per ogni casella nemica calcoliamo tutti i movimenti che quella potrebbe fare
                # supponendo che io abbia fatto quella mossa
                omoves = self._get_correct_moves(opiece, (j, k))

                # se fra le mosse che può fare c'è quella di catturare il re, allora la mossa non si può fare
                if king_pos in omoves:
                    moves.remove(move)
                    break
            self.board.rollback_board()  # rimettiamo la board com'era prima della mossa
        return moves

    def _get_all_player_moves(self, color):
        moves = set()
        for move, piece in self.board.get_pieces(valid=True):
            if piece.color != color:
                continue
            moves = moves.union(self._get_correct_moves(piece, move))
        return list(moves)

    def promote(self, clss):
        # questo metodo viene chiamato solo con la classe con cui si vuole promuovere il pedone,
        # tutto il resto già lo sa
        piece = self.board.get_piece(self.need_promotion)
        if not piece or not isinstance(piece, Pawn):
            return

        # dato che clss è una classe (tipo Rook) io posso fare clss(piece.color) allo stesso modo di
        # come faccio Rook(piece.color)
        new_piece = clss(piece.color)
        # Rimuoviamo il pedone e mettiamo il nuovo pezzo
        self.board.put(self.need_promotion, new_piece)
        self.need_promotion = None
        self.end_turn()

    def change_turn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE

    def update_notation(self, piece, start, end):
        self.notation.append([piece.color, piece.__class__.__name__, start, end])

    def _get_other_player(self, color):
        return WHITE if color == BLACK else BLACK

    def _is_at_the_end(self, position, piece):
        if position[0] == 0 and piece.color == WHITE:
            return True

        elif position[0] == ROWS - 1 and piece.color == BLACK:
            return True
