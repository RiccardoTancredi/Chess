# import pygame
# from dinamics.constants import BLACK_KNIGHT, WHITE_KNIGHT, BLACK, WHITE
#
# class Knight:
#     def __init__(self):
#         # self.color = color
#         self.knight = None
#
#     def knight_color(self, color):
#         if color == WHITE:
#             self.knight = WHITE_KNIGHT
#         else:
#             self.knight = BLACK_KNIGHT
#         return self.knight
#
#     def movements(self):
#         pass

from dinamics.piece import Piece


class Knight(Piece):
    def get_available_moves(self, position):
        return [(0, 0)]  # todo
