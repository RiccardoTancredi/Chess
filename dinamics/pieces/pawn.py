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


class Pawn(Piece):
    def get_available_moves(self, position):
        # current = position # this is the current position of the pawn
        possible_moves = []
        for x in range(position[0]-1, position[0]+2):
            for y in range(position[1], position[1]+2):
                # if board[x][y] == 0 or list(board[x][y]) == [piece for piece in BLACK_PIECES]:
                #     possible_moves.append(x,y)
                # if last_move was made by black pawn and pawns are next to each other and black pown moved by 2:
                #     en passant
                pass
        return [(0, 0)]  # todo
