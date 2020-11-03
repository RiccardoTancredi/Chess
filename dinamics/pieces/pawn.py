from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS, WHITE, BLACK


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True

    def piece_moved(self):
        # This method is made in order to track if a piece has been moved: this is for pawn and particoular moves, like casteling, in which,
        # if the king has already been moved, it can't castle, or if a pawn hasn't been moved yet, it can double jump.

        # TO IMPLEMENT
        # we can now use self.move_history

        return True

    def get_movements(self):
        if len(self.moves_history) == 0:
            return [(0, 1), (0, 2)]

        return [(0, 1)]


        # possible_moves = []
        # if position[0] == 0 or position[0] == ROWS:
        #     # Promotion
        #     pass
        # elif color == BLACK:
        #     possible_moves = [(position[0] + 1, position[1])]
        # else:
        #     possible_moves = [(position[0] - 1, position[1])]
        #
        # return possible_moves

    def delete_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                if self.color == WHITE:
                    for column in range(1, 3):
                        if board.get_piece((position[0]-column, position[1])) and (position[0]-column, position[1]) in moves:
                            for col in range(position[0]-column, -1, -1):
                                if (col, position[1]) in moves:
                                    moves.remove((col, position[1]))
                else:
                    for column in range(1, 3):
                        if board.get_piece((position[0]+column, position[1])) and (position[0]+column, position[1]) in moves:
                            for col in range(position[0]+column, ROWS):
                                if (col, position[1]) in moves:
                                    moves.remove((col, position[1]))
        return moves

    def add_moves(self, board, position, moves):
        if self.color == WHITE:
            # if position[0] - 1 >= 0 and position[1] - 1 >= 0 and position[1] + 1 <= COLS-1:
            if board.get_piece((position[0] - 1, position[1] - 1)):
                moves.append((position[0] - 1, position[1] - 1))
            if board.get_piece((position[0] - 1, position[1] + 1)):
                moves.append((position[0] - 1, position[1] + 1))
        else:
            # if position[0] + 1 <= ROWS-1 and position[1] - 1 >= 0 and position[1] + 1 <= COLS-1:
            if board.get_piece((position[0] + 1, position[1] + 1)):
                moves.append((position[0] + 1, position[1] + 1))
            if board.get_piece((position[0] + 1, position[1] - 1)):
                moves.append((position[0] + 1, position[1] - 1))
        return moves

    def en_passant(self, board, position, moves):
        the_pawn = board.get_piece(position)
        if board.get_piece((position[0], position[1]-1)): # en passant of a pawn to the left
            passant = board.get_piece((position[0], position[1]-1))
            if len(passant.moves_history) == 1:
                if passant.__class__.__name__ == "Pawn" and (passant.moves_history[0][0] == 3 or passant.moves_history[0][0] == 4): #these are the positions where the move can append
                    if passant.color == "BLACK" and the_pawn.color != passant.color:
                        moves.append((position[0]-1, position[1]-1))
                    elif passant.color == "WHITE" and the_pawn.color != passant.color:
                        moves.append((position[0]+1, position[1]-1))
        if board.get_piece((position[0], position[1]+1)): # en passant of a pawn to the right
            passant = board.get_piece((position[0], position[1]+1))
            if len(passant.moves_history) == 1:
                if passant.__class__.__name__ == "Pawn" and (passant.moves_history[0][0] == 3 or passant.moves_history[0][0] == 4): 
                    if passant.color == "BLACK" and the_pawn.color != passant.color:
                        moves.append((position[0]-1, position[1]+1))
                    elif passant.color == "WHITE" and the_pawn.color != passant.color:
                        moves.append((position[0]+1, position[1]+1))
               
        return moves


    def promotion(self, position):
        if self.color == "WHITE" and position[0] == 0:
            pass
        pass
