# import pygame
# from dinamics.constants import BLACK_ROOK, WHITE_ROOK, BLACK, WHITE
#
# class Rook:
#     def __init__(self):
#         # self.color = color
#         self.rook = None
#
#     def rook_color(self, color):
#         if color == WHITE:
#             self.rook = WHITE_ROOK
#         else:
#             self.rook = BLACK_ROOK
#         return self.rook
#
#     def movements(self):
#         pass

from dinamics.piece import Piece


class Rook(Piece):
    def get_available_moves(self, position):
        return [(0, 0)]  # todo
