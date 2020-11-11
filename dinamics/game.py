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
        self.need_promotion = None

    def move_piece(self, start, end, check=True):
        if self.need_promotion:  # se c'è un pezzo da promuovere promuovilo prima di procedere
            return

        piece = self.board.get_piece(start)
        if not piece:
            return

        if check:  # se vogliamo controllare che sia una mossa valida. potremo non volerlo quando usiamo la grafica
            pass  # todo

        self.board.move(start, end, piece)
        piece.on_move(start, end)

        self.update_notation(piece, start, end)

        if isinstance(piece, Pawn) and self._is_at_the_end(end, piece):
            self.need_promotion = end

        if not self.need_promotion:  # Se c'è un pezzo da promuovere non cambiare il turno
            self.change_turn()

    def get_possible_moves(self, position):
        piece = self.board.get_piece(position)
        if not piece:
            return []

        moves = self._get_correct_moves(piece, position)
        moves = self._remove_pinned_moves(position, piece, moves)

        # if isinstance(piece, King):
        #     moves = self._castling(piece, self.board, position, moves)
        if isinstance(piece, Pawn):
            moves = self._en_passant(piece, self.board, position, moves, self.notation)

        for move in list(moves):
            other = self.board.get_piece(move)
            if not other:
                continue

            if other.color == piece.color:
                moves.remove(move)
        return moves

    def _get_correct_moves(self, piece, position):
        moves = piece.get_movements()
        moves = self._add_moves_to_pos(piece, position, moves)
        moves = self._remove_outside_board(moves)
        moves = piece.edit_moves(self.board, position, moves)
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

    # elimina le mosse che sono al di fuori della board
    def _remove_outside_board(self, moves):
        trimmed = []
        for move in moves:
            if (0 <= move[0] < COLS) and (0 <= move[1] < ROWS):
                trimmed.append(move)

        return trimmed

    def _remove_pinned_moves(self, position, piece, moves):

        king_pos = None
        is_king = False
        # se la pedina cliccata è il re
        if isinstance(piece, King):
            king_pos = position
            is_king = True

        else:
            # cerchiamo il re
            for (j, k), opiece in self.board.get_pieces(valid=True):
                if opiece.color != piece.color:
                    continue
                if isinstance(opiece, King):
                    king_pos = (j, k)
                    break

        # remove castling moves if necessary
        r_castling = (king_pos[0], king_pos[1]+2)
        l_castling = (king_pos[0], king_pos[1]-2)

        # per ogni mossa del pezzo che voglio muovere
        for move in list(moves):
            self.board.save_board()  # salviamo la board come è
            # moviamo il pezzo secondo una delle mosse possibili
            # nel move c'è della logica che potrebbe dar problemi
            self.board.move(position, move, piece)
            for (j, k), opiece in self.board.get_pieces(valid=True):  # per ogni pezzo della board
                if opiece.color == piece.color:  # se è un alleato saltiamo
                    continue

                # per ogni casella nemica calcoliamo tutti i movimenti che quella potrebbe fare
                # supponendo che io abbia fatto quella mossa
                omoves = self._get_correct_moves(opiece, (j, k))

                # Se la pedina cliccata è il re e se la pedina nemica mi cattura, togliamo la mossa
                if is_king and move in omoves:
                    if move in moves:
                        moves.remove(move)
                    # if one of the castling squares is under attack it can't castle
                    if move[1] > king_pos[1] and  r_castling in moves:
                        moves.remove(r_castling)
                    if move[1] < king_pos[1] and l_castling in moves:
                        moves.remove(l_castling) 
                    # break

                # se non sono il re e fra le mosse che può fare c'è quella di catturare il re, allora la mossa non si può fare               
                elif not is_king and king_pos in omoves:
                    moves.remove(move)       
                    # break 
                # if the king is under check it can't castle
                if is_king and king_pos in omoves:
                    if r_castling in moves:
                        moves.remove(r_castling)
                if is_king and king_pos in omoves:
                    if l_castling in moves:
                        moves.remove(l_castling)
            self.board.rollback_board()  # rimettiamo la board com'era prima della mossa
        return moves

    def _delete_moves(self, piece, board, position, moves):
        return piece.delete_moves(board, position, moves)

    def _add_moves(self, piece, board, position, moves):
        return piece.add_moves(board, position, moves)

    # def _castling(self, king, board, position, moves):
    #     return king.castling(board, position, moves)

    def _en_passant(self, pawn, board, position, moves, notation):
        return pawn.en_passant(board, position, moves, notation)

    def promote(self, clss):
        # questo metodo viene chiamato solo con la classe con cui si vuole promuovere il pedone,
        # tutto il resto già lo sa
        piece = self.board.get_piece(self.need_promotion)
        if not piece or not isinstance(piece, Pawn):
            return

        # dato che clss è una classe (tipo Rook) io posso fare clss(piece.color) allo stesso modo di
        # come faccio Rook(piece.color)
        new_piece = clss(piece.color)
        self.board.replace(self.need_promotion,
                           new_piece)  # Rimuoviamo il pedone e mettiamo il nuovo pezzo
        self.change_turn()
        self.need_promotion = None

    def change_turn(self):
        self.turn = BLACK if self.turn == WHITE else WHITE

    def update_notation(self, piece, start, end):
        self.notation.append([piece.color, piece.__class__.__name__, start, end])

    def _is_at_the_end(self, position, piece):
        if position[0] == 0 and piece.color == WHITE:
            return True

        elif position[0] == ROWS - 1 and piece.color == BLACK:
            return True
