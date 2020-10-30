# import pygame
# from dinamics.constants import BLACK_PAWN, WHITE_PAWN, BLACK, WHITE
# # from dinamics.piece import Piece
#
# class Pawn:
#     def __init__(self):
#         # self.color = color
#         self.pawn = None
#
#     def pawn_color(self, color):
#         if color == WHITE:
#             self.pawn = WHITE_PAWN
#         else:
#             self.pawn = BLACK_PAWN
#         return self.pawn
#
#     def movements(self):
#         pass

# def make_king(self):
#     self.king = True

# class Pawn(Piece):
#     def __init__(self, color):
#         super().__init__(None, None, color, None, None)
#         self.pawn = None

#     def select(self):
#         if self.color == WHITE:
#             self.pawn = WHITE_PAWN
#         else:
#             self.pawn = BLACK_PAWN
#         return self.pawn

from dinamics.piece import Piece
from dinamics.constants import ROWS, COLS


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True

    def get_available_moves(self, position, color):
        self.color = color
        if position[0] == 0 or position[0] == ROWS:
            # Promotion
            pass
        elif color == "BLACK":
            possible_moves = [(position[0] + 1, position[1])]
        else:
            possible_moves = [(position[0] - 1, position[1])]

        return possible_moves

    def piece_moved(self):
        # This method is made in order to track if a piece has been moved: this is for pawn and particoular moves, like casteling, in which,
        # if the king has already been moved, it can't castle, or if a pawn hasn't been moved yet, it can double jump.

        # TO IMPLEMENT

        return True

    def get_movements_test(self):
        if self.first_move:
            return [(0, 1), (0, 2)]

        return [(0, 1)]

    def on_move(self, start, end):
        if self.first_move:
            self.first_move = False

    def delete_moves(self, board, position, moves):
        for i in range(ROWS):
            for j in range(COLS):
                if self.color == "WHITE":
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

    def eat_piece(self, board, position, moves):
        if self.color == "WHITE":
            if board.get_piece((position[0] - 1, position[1] - 1)):
                moves.append((position[0] - 1, position[1] - 1))
            if board.get_piece((position[0] - 1, position[1] + 1)):
                moves.append((position[0] - 1, position[1] + 1))
        else:
            if board.get_piece((position[0] + 1, position[1] + 1)):
                moves.append((position[0] + 1, position[1] + 1))
            if board.get_piece((position[0] + 1, position[1] - 1)):
                moves.append((position[0] + 1, position[1] - 1))
        return moves
        
