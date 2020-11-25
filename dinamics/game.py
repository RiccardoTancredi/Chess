from dinamics.board import Board, ChessBoard
from dinamics.constants import WHITE, BLACK
from dinamics.constants import ROWS, COLS
from dinamics.pieces.king import King
from dinamics.pieces.pawn import Pawn


class Game:
    PLAYING, CHECKMATE, DRAW = 1, 2, 3  # delle costanti per specificare lo status della partita

    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = ChessBoard()

        self.turn = WHITE
        self.notation = []
        self.need_promotion = None
        self.status = Game.PLAYING  # specifica se il game è finito in checkmate, patta o se è ancora in corso
        self.winner = None  # se il game è finito e c'è un vincitore: checkmate, altrimenti: patta

    def get_possible_moves(self, position):
        piece = self.board.get_piece(position)
        if not piece:
            return []

        moves = self._get_correct_moves(piece, position)
        moves = self._remove_pinned_moves(position, piece, moves)

        return moves

    def move_piece(self, start, end, check=False):
        if self._is_game_ended():
            return

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
        self.change_turn()
        # ad ogni fine turno controlliamo se quello che ha mosso ha vinto o no controllando le mosse dell'altro
        self.status = self._get_game_status(self.turn)  # ritorna se è patta, checkmate o ancora giocabile
        if self.status == Game.CHECKMATE:
            self.winner = self._get_other_player(self.turn)

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

        is_king = False
        if isinstance(piece, King):  # se la pedina cliccata è il re
            king_pos = position
            is_king = True
            moves.append(king_pos)  # aggiungiamo fra le mosse possibile la mosse di stare fermo (spiegato dopo)

        else:  # altrimenti, cerchiamo il re
            king_pos = self._get_king_position(piece.color)
            if not king_pos:  # per i test
                return moves

        can_castle_sx = True
        can_castle_dx = True
        # per ogni mossa del pezzo che voglio muovere
        for move in list(moves):
            self.board.save_board()  # salviamo la board come è
            # moviamo il pezzo secondo una delle mosse possibili
            self.board.move(position, move)
            for (j, k), opiece in self.board.get_pieces(valid=True):  # per ogni pezzo della board
                # se è un alleato saltiamo
                if opiece.color == piece.color:
                    continue

                # per ogni casella nemica calcoliamo tutti i movimenti che quella potrebbe fare
                # supponendo che io abbia fatto quella mossa
                omoves = self._get_correct_moves(opiece, (j, k))

                if is_king and move in omoves:  # quindi il re muovendosi sarebbe sotto scacco
                    if move == king_pos:  # se è la mossa di stare fermo, vuol dire che il re è sotto scacco
                        # di conseguenza non possiamo fare nessun arrocco
                        can_castle_sx = False
                        can_castle_dx = False

                    elif move[0] == king_pos[0]:  # se è una mossa sulla stessa riga
                        if move[1] < king_pos[1]:  # se è una mossa verso sinistra (che è sotto scacco)
                            can_castle_sx = False  # non possiamo arroccare a sx
                        else:
                            can_castle_dx = False  # viceversa, non possiamo arroccare a destra

                    moves.remove(move)  # a prescindere, dato che è una mossa che porterebbe sotto scacco, togliamola
                    break

                # se fra le mosse che può fare c'è quella di catturare il re, allora la mossa non si può fare
                if not is_king and king_pos in omoves:
                    moves.remove(move)
                    break
            self.board.rollback_board()  # rimettiamo la board com'era prima della mossa

        if is_king:
            # se non possiamo arroccare, dobbiamo togliere quelle mosse
            for (j, k) in list(moves):
                if k - king_pos[1] == -2 and not can_castle_sx:  # è un arrocco a sx e non possiamo farlo
                    moves.remove((j, k))
                elif k - king_pos[1] == 2 and not can_castle_dx:
                    moves.remove((j, k))

            if king_pos in moves:  # togliamo la mossa farlocca che avevamo aggiunto all'inizio
                moves.remove(king_pos)

        return moves

    def _get_game_status(self, color):
        # ritorna se il gioco è finito con una vittoria, una patta o è ancora in corso
        check = False
        king_pos = self._get_king_position(color)
        for move, piece in self.board.get_pieces(valid=True):
            if piece.color != color:
                continue
            moves = self.get_possible_moves(move)
            if king_pos in moves:  # se il re è sotto scacco, segnamocelo
                check = True

            if moves:  # appena trovo delle mosse che potrei fare, ritorno che sono ancora in gioco
                return Game.PLAYING

        # se sono qui, vuol dire che non c'è nessuna mossa disponibile
        if check:  # se il re è sotto scacco, allora ho perso
            return Game.CHECKMATE
        else:  # è patta
            return Game.DRAW

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

    def _is_game_ended(self):
        return not self.status == Game.PLAYING

    def _get_king_position(self, color):
        for (j, k), piece in self.board.get_pieces(valid=True):
            if piece.color == color and isinstance(piece, King):
                return j, k

    def _is_at_the_end(self, position, piece):
        if position[0] == 0 and piece.color == WHITE:
            return True

        elif position[0] == ROWS - 1 and piece.color == BLACK:
            return True
