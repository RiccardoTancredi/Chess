# import pygame
# from dinamics.constants import BLACK_BISHOP, WHITE_BISHOP, BLACK, WHITE
#
# class Bishop:
#     def __init__(self):
#         # self.color = color
#         self.bishop = None
#
#     def bishop_color(self, color):
#         if color == WHITE:
#             self.bishop = WHITE_BISHOP
#         else:
#             self.bishop = BLACK_BISHOP
#         return self.bishop
#
#     def movements(self):
#         pass

from dinamics.piece import Piece


class Bishop(Piece):
    def get_available_moves(self, position):
        return [(0, 0)]  # todo