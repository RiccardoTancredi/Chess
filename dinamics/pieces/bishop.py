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

    def get_movements_test(self):
        return [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),      # le 4 possibili L (se sono in (0,0))
                (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),      # le 4 possibili L (se sono in (0,0))
                (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)]
