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
        return [(0, 0)]  # todo
